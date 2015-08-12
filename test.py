# import RPi.GPIO as GPIO
import os
import time
import re
from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop

class BaseRequest(RequestHandler):
    def get(self):
        self.write('test sublime')

app = Application([
    ('/', BaseRequest),
])

if __name__ == '__main__':
    app.listen(80)
    IOLoop.current().start()