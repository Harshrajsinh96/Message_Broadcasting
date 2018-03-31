import zmq
import sys
from threading import Thread

context = zmq.Context()

sender = context.socket(zmq.PUSH)
sender.connect("tcp://127.0.0.1:5678")

user = sys.argv[1]
print("User [%s] Connected to the chat server." %(user))


def subscribe():
    subscriber = context.socket(zmq.SUB)
    subscriber.connect("tcp://127.0.0.1:5677")
    subscriber.setsockopt_string(zmq.SUBSCRIBE, '') 

    while True:
        message = subscriber.recv().decode()
        if(message):
            if ("[{}]:".format(user) not in message):
                print ("\n{}".format(message)+"\n[{}] > ".format(user), end="")
        
def new_thread():
    thread = Thread(target=subscribe)
    thread.start()

new_thread()
while True:
    new_msg = input("[{}] > ".format(user))
    new_msg = "[%s]:  %s" % (user, new_msg)
    sender.send_string(new_msg)