#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Code taken from http://people.csail.mit.edu/albert/bluez-intro/x232.html

import bluetooth
import sys
import numpy as np

def main(args):
    server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

    port = 1
    server_sock.bind(("",port))
    server_sock.listen(1)

    client_sock,address = server_sock.accept()
    print("Accepted connection from {}".format(address))

    #Number inside function is the max number of bytes the socket will be allowed to receive
    data = client_sock.recv(1024) 
    #data must be converted from binary to your desired object type here
    print("received {}".format(data)) 

    client_sock.close()
    server_sock.close()

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
