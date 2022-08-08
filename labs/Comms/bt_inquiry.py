#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Code taken from pybluez github under examples/inquiry.py with some changes 

import bluetooth


#Have to run “sudo hciconfig hci0 piscan” command in terminal once
#before running this code for it to work.
def main(args):
    print("Performing inquiry...")

    nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True,
                                                flush_cache=True, lookup_class=False)

    print("Found {} devices".format(len(nearby_devices)))

    for addr, name in nearby_devices:
        try:
            print("   {} - {}".format(addr, name))
        except UnicodeEncodeError:
            print("   {} - {}".format(addr, name.encode("utf-8", "replace")))

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
