import Tkinter
import threading
import matplotlib
import matplotlib.pyplot
import matplotlib.backends.backend_tkagg

class Plotter():
    def __init__(self,fig):
        self.root = Tkinter.Tk()
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0" % (w, h))
        #self.root.state("zoomed")
        self.fig = fig
        t = threading.Thread(target=self.PlottingThread,args=(fig,))
        t.start()

    def PlottingThread(self,fig):     
        canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=self.root)
        canvas.show()
        canvas.get_tk_widget().pack(side=Tkinter.TOP, fill=Tkinter.BOTH, expand=1)

        toolbar = matplotlib.backends.backend_tkagg.NavigationToolbar2TkAgg(canvas, self.root)
        toolbar.update()
        canvas._tkcanvas.pack(side=Tkinter.TOP, fill=Tkinter.BOTH, expand=1)
        self.root.mainloop()


if __name__=="__main__":
    fig = matplotlib.pyplot.figure()
    Plotter(fig)
    fig.gca().clear()
    fig.gca().plot([1,2,3],[4,5,6])
    fig.canvas.draw()
