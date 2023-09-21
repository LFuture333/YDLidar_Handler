import csv
import Lidar
from datetime import datetime
import pandas as pd
import numpy as np



#Get the usb port of the lidar
port = Lidar.Get_port()

#start the laser & enable the parameters of the lidar 
laser = Lidar.Parameters(port=port)

# initialize the handler of the sdk
ret , scan, laser = Lidar.Initialize_SDK(laser=laser)


#Get time & date for the csv file name
filename = datetime.now()


while True:
    
    #Get the data from the lidar 
    print("New Data")
    x, y = Lidar.Extract_Data(ret=ret, scan=scan, laser=laser)
    for t in range(len(x)):
        print(str(t)+ ") Data Point X: " + str(x[t]) + " Y: " + str(y[t]))

