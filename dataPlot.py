import matplotlib.pyplot as plt
import numpy as np
import time
import threading
import tcpc

def sensorplot():
    # loop to update the data 
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
    sen1f.set_ylim((-10,10))
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
    t=threading.Thread(target=tcpc.client)
    t.start()
    while True:
        try:
            y[:-100] = y[100:]
            y[-100:] = np.random.randn(100)
            #y[-100:] = np.arange(100)
            #y[-1:] = value[0:100]
            # set the new data
            sen1fr.set_ydata(y)
            fig.canvas.draw()
        except KeyboardInterrupt:
            break

if __name__=="__main__":
    #t=threading.Thread(target=tcpc.client)
    #t.start()
    sensorplot()


