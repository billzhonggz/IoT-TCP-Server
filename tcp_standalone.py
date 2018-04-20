import SetupDjangoORM
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
                data = yield stream.read_until(b"\n")
                yield stream.write(data)
                data_string = data.decode("utf-8")
                print(data_string)
                # Write data to ORM.
                rd = RawData(raw_data=data_string)
                rd.save()
            except StreamClosedError:
                break


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
