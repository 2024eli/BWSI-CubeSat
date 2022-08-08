#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Code taken from pybluez github under examples/simple/asynchronous-inquiry.py
#with some changes 

import os
import bluetooth
import select
bt_addr = "B8:27:EB:8E:BB:81 - raspberrypi3" #replace with your pi's bluetooth address

class MyDiscoverer(bluetooth.DeviceDiscoverer):

    def pre_inquiry(self):
        self.RSSI_vals = {} #Will store RSSI value of each device in range every time 
                            #inquiry function is called
        self.done = False

    def device_discovered(self, address, device_class, rssi, name):
        #This function is called whenever a device is discovered while running an inquiry
        self.RSSI_vals[name.decode('utf-8')] = rssi

    def inquiry_complete(self):
        self.done = True
        
        
def inquiry(d, duration):
    d.find_devices(lookup_names=True, duration=duration)
    
    readfiles = [ d, ]

    while True:
        rfds = select.select( readfiles, [], [] )[0]

        #Basically checking if d is a readable file, and if it is 
        #calls process_event which either discovers a new device or ends the inquiry.
        #When inquiry is ended d.done is set to true becaues of inquiry_complete function
        if d in rfds:
            d.process_event()

        if d.done: break



def find_num_bytes():
    """
    Finds number of bytes sent and received using bluetooth on this device.
    
    Returns:
        Number of bytes sent and received using bluetooth
        Tuple with two ints
        (total amount of bytes received, total amount of bytes transmitted)
    """
    
    stream = os.popen('hciconfig inqtpl') #Run this command in terminal
    output = stream.read()
    #Go through text outputted by the command and take out the numbers we want
    RX_bytes = output[output.find('RX bytes') + 9: output.find('acl') - 1]
    TX_bytes = output[output.find('TX bytes') + 9: output.rfind('acl') - 1]
    return (int(RX_bytes), int(TX_bytes))
    


def main(args):
    #If you want to plot RSSI values using pyplot, use the RSSI_vals
    #dictionary and for loop
    
    NUM_INQS = 1 #Number of times to repeat an inquiry
    INQ_TIME = 8 #Amount of seconds to wait for each inquiry
    
    d = MyDiscoverer()
    
    for i in range(NUM_INQS):
        print('Performing inquiry {}'.format(i + 1))
        
        inquiry(d, INQ_TIME)
        for name, rssi in d.RSSI_vals.items():
            print("Name: {} \nRSSI: {}".format(name, rssi))
        
        RX, TX = find_num_bytes()
        print('RX bytes: {} \nTX bytes: {} \n'.format(RX, TX))
    
            

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
