""" EE 250L Lab 02: GrovePi Sensors

List team members here.

Insert Github repository link here.
"""

"""python3 interpreters in Ubuntu (and other linux distros) will look in a 
default set of directories for modules when a program tries to `import` one. 
Examples of some default directories are (but not limited to):
  /usr/lib/python3.5
  /usr/local/lib/python3.5/dist-packages

The `sys` module, however, is a builtin that is written in and compiled in C for
performance. Because of this, you will not find this in the default directories.
"""
import sys
import time
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('../../Software/Python/')
# This append is to support importing the LCD library.
sys.path.append('../../Software/Python/grove_rgb_lcd')

import grovepi
import decimal
from grove_rgb_lcd import *

"""This if-statement checks if you are running this python file directly. That 
is, if you run `python3 grovepi_sensors.py` in terminal, this if-statement will 
be true"""
if __name__ == '__main__':
    PORT = 4    # D4
    POTENTIOMETER = 0 #A0
    a = 250
    b = 250
    c = 250
    dist = ""
    olddist = dist
    rangenum = 0
    rangestr = str(rangenum)
    oldrangenum = rangenum
    oldrangestr = rangestr
    while True:
        #So we do not poll the sensors too quickly which may introduce noise,
        #sleep for a reasonable time of 200ms between each iteration.
        time.sleep(0.2)
        setRGB(a,b,c)
        dist = str(grovepi.ultrasonicRead(PORT))
        rangenum = grovepi.analogRead(POTENTIOMETER)
        #convert range of 0-1024 values from potentiometer to 0-517ish centimeters range of sonic sensor
        rangenum = int(rangenum/2)
        rangestr = str(rangenum)
        if(dist != olddist or rangenum != oldrangenum):
            
            if(int(dist) <= rangenum):
                #if object IS in range
                setText_norefresh(rangestr + "cm OBJ PRES "+ "\n" + dist + "cm")
            else:    
                #if object IS NOT in range
                setText_norefresh(rangestr + "cm          "+ "\n" + dist + "cm")
            
            olddist = dist
            oldrangenum = rangenum
            #time.sleep(0.2)
        #setText("Reading: " + dist)
        #print(grovepi.ultrasonicRead(PORT))
        
        
