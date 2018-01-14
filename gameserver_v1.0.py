import socket
from queue import *
import threading
import time

NUMBER_OF_THREADS = 3
JOB_NUMBER = [1, 2]
queue = Queue()
all_connections = []
all_addresses = []




# create socket (allows computers to connect)
def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 13300
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error:" + str(msg))

# Bind socket to port and wait for connection from client
def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding socket to port: " + str(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("Socket binding error: " + str(msg) + "\n" + "Retrying...")
        socket_bind()




# Accept connection from multiple clients and save to list
def accept_connections():
    for c in all_connections:
        c.close()
    del all_connections[:]
    del all_addresses[:]
    while 1:
        try:
            conn, address = s.accept()
            conn.setblocking(1)
            all_connections.append(conn)
            all_addresses.append(address)
            print("\nConnection has been established: " + address[0])
        except:
            print("Error accepting connections")


#create worker threads
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

#do the next job in queue (one handles connections, other sends commands)
def work():
    while True:
        x = queue.get()
        if x == 1:
            socket_create()
            socket_bind()
            accept_connections()
        if x == 2:
            start_adminconsole()
        #queue.task_done()


def create_jobs():
    for x in JOB_NUMBER:
        queue.put(x)
    queue.join()


#list connections
def list_connections():
    print(all_addresses[:])


#interactive admin console
def start_adminconsole():
    while True:
        cmd = input('Admin> ' )
        if cmd == 'list':
            connections = list_connections()
            if connections == None:
                connections = ''
            print(connections, end='')
        elif cmd == 'quit':
            for c in all_connections:
                c.close()
            del all_connections[:]
            del all_addresses[:]
            quit()
        elif cmd == None:
            continue
        else:
            continue



create_workers()
create_jobs()










































