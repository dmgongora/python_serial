#--------------------------------------------------------------------#
# Description: Read serial port.
#--------------------------------------------------------------------#
import serial, time
from collections import deque
    
serdev = '/dev/ttyACM0'
#serdev = '/dev/ttyUSB1'
mbed = serial.Serial(serdev) 
#mbed.baudrate = 921600 #9600 #921600 # 115200, 921600
mbed.baudrate = 9600#57600#9600#921600#115200#
mbed.timeout = 0.000150
mbed.rtscts = True
mbed.dsrdtr = True

print 'Initializing serial port monitor.'
print mbed
samples_buffer = deque()

time.sleep(1)

print 'Receiving signals...'
time.sleep(1)
temp = ''
currentItem = 0
readBuffer = False

loopDur = 600 # in seconds
currentTime = time.time() # in seconds
executionTime = currentTime + loopDur

#mbed.write('s')
mbed.flushOutput()
mbed.flushInput()
while executionTime > currentTime:
    if (mbed.inWaiting()) > 0:
        samples_buffer.append( mbed.read( mbed.inWaiting() ) )
    try:
        temp_buffer = (samples_buffer.pop())
        print str(temp_buffer)
    except IndexError:
        time.sleep(0.1)
    currentTime = time.time() # in seconds

# End connection with the uC
mbed.close()





