import sys
import socket
from os import _exit as quit

def main():
    # parse arguments
    if len(sys.argv) != 4:
        print("usage: python3 %s <host> <port> <port>" % sys.argv[0]);
        quit(1)
    host = sys.argv[1]
    bob_port = sys.argv[2]
    mallory_port = sys.argv[3]

    # connect to bob
    # open a client socket
    clientfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to server
    clientfd.connect((host, int(bob_port)))


     # connect to alice
     # open a listen socket
    listenfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listenfd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # bind socket to ip and port
    listenfd.bind(('', int(mallory_port)))

    # listen to socket
    listenfd.listen(1)

    # accept connection
    (connfd, addr) = listenfd.accept()

    # message loop
    while(True):
        msg = connfd.recv(1024).decode()
        print("Received from client: %s" % msg)

        slct = input("Type 1 to delete message, Type 2 to change message sent or Type 3 to send original message\n")
        if int(slct) == 1:
            break
        elif int(slct) == 2:
            msg = input('type new message \n')
            clientfd.send(msg.encode())
        elif int(slct) == 3:
            clientfd.send(msg.encode())





        #        # You don't need to receive for this assignment, but if you wanted to
#        # you would use something like this
#        msg = clientfd.recv(1024).decode()
#        print("Received from server: %s" % msg)

    # close connection
    clientfd.close()

if __name__ == "__main__":
    main()


