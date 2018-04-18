from tornado.ioloop import IOLoop
from tornado.tcpserver import TCPServer
from tornado.iostream import StreamClosedError
from tornado import gen

from django.conf import settings
from tcp.models import *

settings.configure(
    DATABASE_ENGINE='django.db.backends.sqlite3',
    DATABASE_NAME='os.path.join(BASE_DIR, \'db.sqlite3\')',
)

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

if __name__ == '__main__':
    status = run_tcp_server()
    print(status)