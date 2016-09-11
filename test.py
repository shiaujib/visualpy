import matplotlib.pyplot as plt
import numpy as np
import time
import threading

def sensorplot():
    fig = plt.figure()
    ax = fig.add_subplot(211)
    bx = fig.add_subplot(212)

    # some X and Y data
    x = np.arange(1000)
    y = np.random.randn(1000)

    sx = np.arange(10000)
    sy = np.random.randn(10000)
    li, = ax.plot(x, y)
    sc, = bx.plot(sx,sy)

    # draw and show it
    fig.canvas.draw()
    plt.show(block=False)

    # loop to update the data

    while True:
            try:
                y[:-100] = y[100:]
                y[-100:] = np.random.randn(100)

                # set the new data
                li.set_ydata(y)

                fig.canvas.draw()

                #time.sleep(0.01)
            except KeyboardInterrupt:
                break

if __name__=="__main__":
    sensorplot()
    #t=threading.Thread(target=sensorplot)
    #t.start()


