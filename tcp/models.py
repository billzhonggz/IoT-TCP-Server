from django.db import models
from tornado.ioloop import IOLoop
from tornado.tcpserver import TCPServer
from tornado.iostream import StreamClosedError
from tornado import gen


# Create your models here.


class IotTcpServer(TCPServer):
    @gen.coroutine
    def handle_stream(self, stream, address):
        while True:
            try:
                data = yield stream.read_until(b"\n")
                yield stream.write(data)
                data_string = data.decode("utf-8")
                print(data_string)
            except StreamClosedError:
                break


if __name__ == '__main__':
    server = IotTcpServer()
    server.listen(9876)
    print('TCP server is running.')
    IOLoop.current().start()
