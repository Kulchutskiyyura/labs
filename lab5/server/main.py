import socket
import pickle
from Socket_Message import Socket_Message
from Facade import Facade
print("work")

while True:
    print("0")
    sock = socket.socket()
    sock.bind(('', 9090))
    sock.listen(1)
    conn, addr = sock.accept()

    print("1")
    print ('connected:', addr)

   
    data :Socket_Message = pickle.loads(conn.recv(1024))
    if data.action=="start_game":
         server=Facade()
         print("start game")
         server.start_game(0)
         information=server.make_choose(True)
    elif data.action=="save":
         server.save()
         information="work"
    elif data.action=="back":
         information=server.back()
    elif data.action=="make_choose":
         information=server.make_choose(False,data.data)

    conn.send(pickle.dumps(information))

    conn.close()



