import zmq

context = zmq.Context()
subscriber = context.socket(zmq.SUB)

subscriber.connect('tcp://127.0.0.1:9876')
subscriber.setsockopt_string(zmq.SUBSCRIBE, '')


while True:
    print(subscriber.recv_pyobj())
