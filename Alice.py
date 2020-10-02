import sys
import socket
from os import _exit as quit
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from datetime import datetime, timedelta
from gen import generate_keys

def main():
    # parse arguments
    if len(sys.argv) != 5:
        print("usage: python3 %s <host> <port>" % sys.argv[0]);
        quit(1)
    host = sys.argv[1]
    port = sys.argv[2]

    # open a socket
    clientfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to server
    clientfd.connect((host, int(port)))

    # message loop
    while(True):

        if sys.argv[4] == 1:
            msg = ktpt()
            clientfd.send(msg.encode())


#        # You don't need to receive for this assignment, but if you wanted to
#        # you would use something like this
#        msg = clientfd.recv(1024).decode()
#        print("Received from server: %s" % msg)

    # close connection
    clientfd.close()

if __name__ == "__main__":
    main()

def ktpt():
    alice_ident="Alice"
    #hardcoding bob ident
    bob_ident="Bob"

    key = os.urandom(32)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))

    msg = input('input message to be dechipherd\n')
    # need to pad to multiple of 16 chars


    while len(msg) % 16 != 0:
        msg = msg + "0"

    msg = str.encode(msg)+key
    encryptor = cipher.encryptor()
    ctm = encryptor.update(str.encode(msg)) + encryptor.finalize()
    tstamp = datetime.now()

    fullmsg = (bob_ident,tstamp,ctm)

    return fullmsg
