from abc import ABC, abstractmethod
from Socket_Message import Socket_Message
import pickle
import socket
class Command(ABC):
    _host=None
    _port=None
    @abstractmethod
    def execute(self):
        pass
    @staticmethod
    def set_host(host):
       print("set_receiver is on")
       Command._host=host
    @staticmethod
    def set_port(port):
       print("set_receiver is on")
       Command._port=port


class Save_command(Command):
    def execute(self):
        sock = socket.socket()
        sock.connect((Command._host, Command._port))
        message=Socket_Message("save")
        sock.send(pickle.dumps(message))

        self.data = pickle.loads(sock.recv(1024))
        sock.close()



class Back_command(Command):
    def execute(self):
        sock = socket.socket()
        sock.connect((Command._host, Command._port))
        message=Socket_Message("back")
        sock.send(pickle.dumps(message))

        self.data = pickle.loads(sock.recv(1024))
        sock.close()


class Choose_command(Command):
    def execute(self,index_of_choose=0):
        sock = socket.socket()
        sock.connect((Command._host, Command._port))
        message=Socket_Message("make_choose",index_of_choose)
        sock.send(pickle.dumps(message))

        self.data = pickle.loads(sock.recv(1024))
        sock.close()

class Start_command(Command):
    def execute(self):
        sock = socket.socket()
        sock.connect((Command._host, Command._port))
        message=Socket_Message("start_game")
        sock.send(pickle.dumps(message))

        self.data = pickle.loads(sock.recv(1024))
        print(self.data)
        sock.close()
