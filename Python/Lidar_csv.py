import Lidar
import csv
from datetime import datetime

#Get the usb port of the lidar
port = Lidar.Get_port()

#start the laser & enable the parameters of the lidar 
laser = Lidar.Parameters(port=port)

# initialize the handler of the sdk
ret , scan, laser = Lidar.Initialize_SDK(laser=laser)


#Get time & date for the csv file name
filename = str(datetime.now())

header = ['X', 'Y', 'Date & Time']

with open(filename+".csv", 'w',encoding='UTF8', newline='') as f: 
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()
    while True:
        # Lidar data 
        x, y = Lidar.Extract_Data(ret=ret, scan=scan, laser=laser)
        # Get Time for the data set 
        Date_Time =  datetime.now()

        rows=[
            {'X': x,
             'Y': y,
             'Date & Time': str(Date_Time)
            }
        ]

        writer.writerows(rows)

