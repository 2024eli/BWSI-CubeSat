from Cam.area_calc import area_calc
from Cam.sector_area import sector_area
from btcon import *
import time

#ground processing and testing code

connection = BTCon('raspberrypi4')
connection.connect_as_host(1)
print(connection.receive_string())
connection.close_host()

time.sleep(5)

connection = BTCon('raspberrypi4')
connection.connect_as_host(1)
print(connection.receive_string())
connection.close_host()

time.sleep(1)

i = 0
while True: 

    #loop bluetooth receive commands (pls make this work)
    connection = BTCon('raspberrypi4')
    connection.connect_as_host(1)
    location = connection.receive_string()
    timeStamp = connection.receive_string()
    print(connection.receive_image("/home/pi/BloomCube/ReceiveImages/Received" + str(i) + ".jpg"))
    connection.close_host()

    area  = area_calc("Received" + str(i) + ".jpg")
    sector = sector_area(float(location))
    with open('/home/pi/BloomCube/telemetry.txt', 'a') as f:
        f.write('Recieved ' + str(i))
        f.write('\n')
        f.write('Area of bloom: ' + str(area))
        f.write('\n')
        f.write('Sector: ' + str(sector))
        f.write('\n')
        f.write('Location: ' + location)
        f.write('\n')
        f.write('Time Stamp: ' + timeStamp)
        f.write('\n')
    i += 1
