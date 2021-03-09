#Import declerations
import serial
import time

#COM PORT SETTINGS
COM_PORT = 'COM7'
BAUDRATE = 19200
BYTESIZE = 8
PARITY   = serial.PARITY_EVEN
STOPBITS = serial.STOPBITS_ONE
TIMEOUT  = 1000

#COMMUNICATION SETTINGS
BYTES_TO_WRITE = 64

#COM Port configuration
serial_device = serial.Serial(port=COM_PORT,baudrate=BAUDRATE,bytesize=BYTESIZE,parity=PARITY,stopbits=STOPBITS,timeout=TIMEOUT)
#Close serial port in case it was open
serial_device.close()
#Open COM Port
serial_device.open()
#Check if serial device is open
serial_device.is_open
#Write data
while 1:
    time.sleep(1)
    write = serial_device.write((123123123123).to_bytes(BYTES_TO_WRITE,byteorder='big'))
    read = serial_device.read(10)
#Print serial
    print(read)
    
    
