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
                # Write data to ORM.
                RawData.set_raw_data(RawData, data_string)
            except StreamClosedError:
                break


class RawData(models.Model):
    receive_date_time = models.DateTimeField('Record received')
    raw_data = models.CharField(max_length=100)

    def set_raw_data(self, data):
        self.raw_data = data

    def __str__(self):
        return self.id


class ServerOperation(models.Model):
    status_change_date_time = models.DateTimeField('Status changed')
    status = models.BooleanField()

    def run_tcp_server(self):
        iot_tcp_server = IotTcpServer()
        iot_tcp_server.listen(9876)
        IOLoop.current().start()
        self.status = True
        return 'Running'

    def stop_tcp_server(self):
        IOLoop.current().stop()
        self.status = False
        return 'Stopped'

    def __str__(self):
        return self.id


# TEMP: Unit test.
if __name__ == '__main__':
    status = ServerOperation.run_tcp_server(ServerOperation)
    print(status)
