# -*- coding: utf-8 -*-
"""
A script plot plot the data coming from a serial port
Written to monitor the Co2 levels in NoPo nanotechnologies reactor.
Author: Sujay HG

"""
import serial # import Serial Library
import numpy  # Import numpy
import matplotlib.pyplot as plt #import matplotlib library
from drawnow import *
#import random

co2= []
arduinoData = serial.Serial('com26', 9600) #Creating our serial object named arduinoData
plt.ion() #Tell matplotlib you want interactive mode to plot live data
cnt=0

def makeFig(): #Create a function that makes our desired plot
    plt.ylim(0,10000)                                 #Set y min and max values
    plt.title('CO2 sensor Data')      #Plot the title
    plt.grid(True)                                  #Turn the grid on
    plt.ylabel('ppm')                            #Set ylabels
    plt.plot(co2, 'ro-', label='CO2')       #plot the temperature
    plt.legend(loc='upper left')                    #plot the legend
    
while True: # While loop that loops forever
    while (arduinoData.inWaiting()==0): #Wait here until there is data
        pass #do nothing
    arduinoString = arduinoData.readline() #read the line of text from the serial port
 #   arduinoString=random.randint(0,2000)
    print arduinoString
    temp = float( arduinoString)   
         #Convert to floating number and put in temp
    co2.append(temp)                     #Build our tempF array by appending temp readings
    drawnow(makeFig)                       #Call drawnow to update our live graph
    plt.pause(.000001)                     #Pause Briefly. Important to keep drawnow from crashing
    cnt=cnt+1
    if(cnt>50):                            #If you have 50 or more points, delete the first one from the array
        co2.pop(0)                       #This allows us to just see the last 50 data points

