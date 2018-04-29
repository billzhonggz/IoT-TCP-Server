import SetupDjangoORM
from datetime import datetime
from pytz import UTC
from ConvertCoordination import transform
from tcp.models import *

from tornado.ioloop import IOLoop
from tornado.tcpserver import TCPServer
from tornado.iostream import StreamClosedError
from tornado import gen


class IotTcpServer(TCPServer):
    @gen.coroutine
    def handle_stream(self, stream, address):
        while True:
            try:
                data = yield stream.read_until(b"$")
                yield stream.write(data)
                # print(data)
                data_string = data.decode("utf-8")
                print(data_string)
                # Logging
                rd = RawData(raw_data=data_string)
                rd.save()
                # Save valid data.
                handle_data(data_string)
            except StreamClosedError:
                break


def handle_data(raw_data):
    '''
    :param raw_data: Input string receive from the device.
    Following the following format.
    @@356802031957755,023,07.3897,113,17.9050,18.9,20180401143519.000,136,0152500,4140800,1,1,1,1,1,1##$
    @@IMEI(模块ID),纬度(度),纬度(分),经度(度),经度(分),高度,UTC时间,首次定位时间(s),动力电池电压(数据*2=V伏特，2待定),
      备份锂电池电压(数据/1000000=V伏特),锁是否打开(1未开,2开),报警器是否报警(1未报警,2报警),震动报警(还没想好反正1个字符),
      锁模式(1常开,2常闭),报警器模式(1常开,2常闭),无刷控制器锁模式(1常开,2常闭)##$
    :return:
    '''
    # First: Split the string.
    splited = split_data(raw_data)
    # Second: Handle coordinates.
    coordinates = handle_coordinates(splited[1], splited[2], splited[3], splited[4])
    # Third: Handle datetime.
    dt = handle_datetime(splited[6])
    # Fourth: Creating objects.
    # Check whether device record exists.
    try:
        dev = Device.objects.get(imei=splited[0])
    except Device.DoesNotExist:
        print('Create new Device object.')
        dev = Device(imei=splited[0])
        dev.save()
    location = Location(
        device=dev,
        time=dt,
        lat=coordinates[0],
        long=coordinates[1],
        height=splited[5],
        initial_locate_duration=splited[7]
    )
    location.save()
    alarm = Alarm(
        device=dev,
        time=dt,
        power_voltage=float(splited[8]) * 2,
        backup_voltage=float(splited[9]) / 1000000,
        lock_status=splited[10],
        alarm_status=splited[11],
        vibrate_alarm_status=splited[12],
        lock_mode=splited[13],
        alarm_mode=splited[14],
        brushless_control_mode=splited[15],
    )
    alarm.save()


def split_data(raw_data):
    if raw_data[:2] == '@@':
        data = raw_data[2:-3]
        return data.split(',')


def handle_datetime(datetime_string):
    # Throw away decimal numbers.
    datetime_string = datetime_string[:-4]
    dt1 = datetime.strptime(datetime_string, '%Y%m%d%H%M%S')
    dt1 = dt1.replace(tzinfo=UTC)
    return dt1


def handle_coordinates(lat_degrees, lat_minutes, long_degrees, long_minutes):
    # Convert to degrees only.
    lat = int(lat_degrees) + float(lat_minutes) / 60
    long = int(long_degrees) + float(long_minutes) / 60
    # Convert to Mars coordinate.
    trans = transform(lat, long)
    print(trans)
    return trans


def run_tcp_server():
    try:
        iot_tcp_server = IotTcpServer()
        iot_tcp_server.listen(9876)
        IOLoop.current().start()
        so1 = ServerOperation(status=True)
        so1.save()
        return 'TCPServer started.'
    except:
        return 'TCPServer start up failed.'


def stop_tcp_server():
    try:
        IOLoop.current().stop()
        so2 = ServerOperation(status=False)
        so2.save()
        return 'TCPServer stopped.'
    except:
        return 'TCPServer stop failed.'


# TEMP: Unit test.
if __name__ == '__main__':
    status = run_tcp_server()
    print(status)
