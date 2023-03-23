import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
from io import StringIO

class System: 

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.fft = sc.fft(y)
        self.peaks = sc.find_peaks(self.fft)

    def find_peaks(self):
        sc.signal.find_peaks(self.x)

def draw_figure():

    x = np.arange(0,np.pi*3,.1)
    y = np.sin(x)

    fig = plt.figure()
    plt.plot(x,y)

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data