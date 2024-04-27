
import cv2
import matplotlib.pyplot as plt
import sys
import numpy as np
sys.path.append('algorithms')
import hmap as k
import json

def getter () :

    with open('data/raw/xy_data.json', 'r') as f:
        data = json.load(f)
    x = data['x']
    y = data['y']
    return x,y

def start ():
    X,Y = getter()
    x_mesh, y_mesh ,xc , yc,h= k.mesh(X, Y)
    intensity_l = k.distance(xc,yc,X,Y,h)
    inten = np.array(intensity_l)
    plt.pcolormesh(x_mesh,y_mesh,inten)
    plt.plot(X,Y,'ro')
    plt.colorbar()
    plt.show()

    
