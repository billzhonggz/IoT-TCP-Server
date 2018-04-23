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
                splited = split_data(data_string)
                print(splited)
                # Handle coordinates
                coordinates = handle_coordinates(splited[1], splited[2], splited[3], splited[4])
                print(coordinates)
                # Handle time
                dt = handle_datetime(splited[6])
                print(dt)
                # Write data to ORM.
                # rd = RawData(raw_data=data_string)
                # rd.save()
            except StreamClosedError:
                break


def split_data(raw_data):
    if raw_data[:2] == '@@':
        data = raw_data[2:-2]
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
