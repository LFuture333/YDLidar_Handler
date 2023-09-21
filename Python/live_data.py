import numpy as np
import matplotlib.pyplot as plt

import Lidar



port = Lidar.Get_port();

laser = Lidar.Parameters(port)




ret, scan, laser = Lidar.Initialize_SDK(laser)
while True:
    
    x, y = Lidar.Extract_Data(ret, scan, laser)

    plt.clf()
    plt.scatter(x,y)
    plt.pause(.1)

plt.show()