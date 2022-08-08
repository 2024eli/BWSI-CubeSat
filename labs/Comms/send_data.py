#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Code taken from http://people.csail.mit.edu/albert/bluez-intro/x232.html

import bluetooth
import select
import numpy as np
import time

bt_addr = "B8:27:EB:8E:BB:81" #Fill in with your pi's bluetooth address

def main(args):
    port = 1

    sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
    sock.connect((bt_addr, port))
    
    print('Connected, sending data')
    data =  "Hello World" #whatever data you want to send using bluetooth
    sock.send(data)

    sock.close()
    print('Connection closed')


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
