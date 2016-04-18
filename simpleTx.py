#--------------------------------------------------------------------#
# Description: Read serial port.
#--------------------------------------------------------------------#
import serial, time
from collections import deque
    
serdev = '/dev/ttyACM0'
mbed = serial.Serial(serdev)  # Error nro. 16
mbed.baudrate = 921600 #9600 #921600 # 115200, 921600
mbed.timeout = 0.000150
mbed.rtscts = True
mbed.dsrdtr = True
mbed.writeTimeout = 2

print 'Initializing serial port monitor.'
print mbed

mbed.flushInput()
mbed.flushOutput()
time.sleep(1)

print 'Sending signals...'
time.sleep(1)
temp = ''
currentItem = 0
readBuffer = False
#mbed.write('l')

loopDur = 600 # in seconds
currentTime = time.time() # in seconds
executionTime = currentTime + loopDur

while executionTime > currentTime:
    commandToRobot = raw_input("Insert text:")
    mbed.write(commandToRobot)
    mbed.flush()
    #mbed.write(commandToRobot+'\n')
    time.sleep(1)
    currentTime = time.time() # in seconds

# End connection with the uC
mbed.close()


