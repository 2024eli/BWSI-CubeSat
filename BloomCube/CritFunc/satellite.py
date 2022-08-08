from multiprocessing import connection
from btcon import BTCon
import time

time.sleep(10)
connection = BTCon('raspberrypi3')
status = connection.connect_as_client(1)
seconds = time.time()
good = time.ctime()

while status == False:
    connection = BTCon('raspberrypi3')
    status = connection.connect_as_client(1)

timeStamp = "Time created " + good
connection.write_string(timeStamp)
connection.close_client()

