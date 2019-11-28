import socket
from _thread import *
import threading

connected_clients = 0

# thread fuction
def handle_new_client(c):
    global connected_clients
    connected_clients += 1
    f = c.makefile()
    line = f.readline()
    f.close()
    c.send(line.encode('utf8'))
    c.close()
    connected_clients -= 1

def Main(): 
    # reverse a port on your computer 
    # in our case it is 12345 but it 
    # can be anything 
    port = 8080
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind(('0.0.0.0', port)) 
    print("socket binded to port", port) 
  
    # put the socket into listening mode 
    s.listen(5) 
    print("socket is listening") 
  
    # a forever loop until client wants to exit 
    while True: 
        # establish connection with client 
        c, addr = s.accept() 
        print('Connected to :', addr[0], ':', addr[1]) 
  
        # Start a new thread and return its identifier 
        start_new_thread(handle_new_client, (c,)) 
    s.close()
  
  
if __name__ == '__main__': 
    Main()


