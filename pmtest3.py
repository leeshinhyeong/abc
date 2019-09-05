import serial
import time

def hexShow(argv):  
   result = ''  
   hLen = len(argv)  
   for i in xrange(hLen):  
       hvol = ord(argv[i])  
       hhex = '%02x'%hvol  
       result += hhex+' '  
 
t = serial.Serial('/dev/ttyUSB0',9600)  
while True:
   t.flushInput()
   time.sleep(1.5)
   retstr = t.read(10)
   hexShow(retstr)
   if len(retstr)==10:
       if(retstr[0]==b"\xaa" and retstr[1]==b'\xc0'):
           checksum=0
           for i in range(6):
               checksum=checksum+ord(retstr[2+i])
           if checksum%256 == ord(retstr[8]):
               pm25=ord(retstr[2])+ord(retstr[3])*256
               pm10=ord(retstr[4])+ord(retstr[5])*256
               print "pm2.5:%.1f pm10 %.1f"%(pm25/10.0,pm10/10.0)