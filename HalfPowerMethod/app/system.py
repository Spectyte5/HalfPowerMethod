import numpy as np
from scipy.signal import find_peaks
from scipy import signal
import matplotlib.pyplot as plt
from io import StringIO

class System: 

    def __init__(self,sys,freq_range):
        self.freq = freq_range
        _, self.fft = signal.freqresp(sys, 2 * np.pi * freq_range)
        self.q = []
        self.damping = []
        self.nat = []
 
    def my_figure():
        fig, ax = plt.subplots()
        ax.plot([1, 3, 4], [3, 2, 5])
        return fig
    
    def calc_damping(self):
        mag = np.abs(self.fft)
        idx = np.argmax(mag)
        mag_half = mag[idx] / np.sqrt(2)
        idx_left = np.argmin(np.abs(mag[:idx] - mag_half)) if idx > 0 else 0
        idx_right = np.argmin(np.abs(mag[idx:] - mag_half)) + idx if idx < len(mag)-1 else len(mag)-1
        f1, f2 = self.freq[idx_left], self.freq[idx_right]
        freq_nat = self.freq[idx]
        Q = freq_nat / (f2 - f1)
        damp = 1 / (2 * Q)
        self.nat.append(freq_nat)
        self.q.append(Q)
        self.damping.append(damp)

def draw_figure(x,y):

    fig = plt.figure()
    plt.plot(x,y)
    plt.xlabel("Freq (Hz)")
    plt.ylabel("Magnitude (a.u)")

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data