from django.db import models
from tornado.ioloop import IOLoop
from tornado.tcpserver import TCPServer

# Create your models here.


class IotTcpServer(TCPServer):
    def handle_stream(self, stream, address):
        def got_data(data):
            print "Input: {}".format(repr(data))
            stream.write("OK", stream.close)

        stream.read_until("\n", got_data)


if __name__ == '__main__':
    server = IotTcpServer()
    server.listen(9876)
    IOLoop.instance().start()