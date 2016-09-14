import matplotlib.pyplot as plt
import numpy as np
import time
import threading
import tcpc
import sys

tmp=[0]*100
result=[10]*100

def sensorplot():
    # loop to update the data 
    global result
    value=[3]*100
    zero=[0]*1000
    fig = plt.figure()
    sen1f = fig.add_subplot(211)
    sen2f = fig.add_subplot(212)
    # some X and Y data
    x = np.arange(100)
    y = zero[0:100]
    sen1f.set_ylabel('value')
    sen1f.set_xlabel('time')
    sen1f.set_ylim((0,20))
    sen1f.set_xlim((0,100))
    sx = np.arange(10000)
    sy = np.random.randn(10000)
    sen2f.set_ylabel('value')
    sen2f.set_xlabel('time')
    sen2f.set_ylim((-10,10))
    sen2f.set_xlim((0,1000))
    sen1fr, = sen1f.plot(x, y)
    sen2fr, = sen2f.plot(sx,sy)
    # draw and show it
    fig.canvas.draw()
    plt.show(block=False)
    t=threading.Thread(target=tcpc.client,args=(result,))
    t.start()
    while True:
        try:
            y[:-99] = y[99:]
            #y[-100:] = np.random.randn(100)
            #y[-100:] = np.arange(100)
            y[-99:] = result[0:99]
            # set the new data
            print result[10]
            sen1fr.set_ydata(y)
            fig.canvas.draw()
        except KeyboardInterrupt:
            break

if __name__=="__main__":
    #t=threading.Thread(target=tcpc.client)
    #t.start()
    sensorplot()


