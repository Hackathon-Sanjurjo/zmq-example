import zmq
import time

context = zmq.Context()
publisher = context.socket(zmq.PUB)

publisher.bind('tcp://127.0.0.1:9876')

while True:
    publisher.send_pyobj('Hello world')
    time.sleep(1)
