import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from io import StringIO

class System: 

    def __init__(self,sys):
        self.freq, self.fft = signal.freqresp(sys)
        self.mag = np.abs(self.fft)
        self.q = []
        self.damping = []
        self.nat = []
        self.peaks = []
 
    def my_figure():
        fig, ax = plt.subplots()
        ax.plot([1, 3, 4], [3, 2, 5])
        return fig
    
    def calc_damping(self):
        self.peaks,_ = signal.find_peaks(self.mag)
        for idx in self.peaks:
            mag_half = self.mag[idx] / np.sqrt(2)
            idx_left = np.argmin(np.abs(self.mag[:idx] - mag_half)) 
            idx_right = np.argmin(np.abs(self.mag[idx:] - mag_half)) + idx 
            f1, f2 = self.freq[idx_left], self.freq[idx_right]
            freq_nat = self.freq[idx]
            Q = freq_nat / (f2 - f1)
            damp = 1 / (2 * Q)
            self.nat.append(freq_nat)
            self.q.append(Q)
            self.damping.append(damp)

    def draw_figure(self):
        fig = plt.figure()
        plt.plot(self.freq,self.mag)
        idx = self.peaks
        plt.plot(self.freq[idx], self.mag[idx], "+")
        plt.xlabel("Freq (Rad/s)")
        plt.ylabel("Magnitude (a.u)")
        plt.title("Frequency Response of the system")
        imgdata = StringIO()
        fig.savefig(imgdata, format='svg', transparent=True)
        imgdata.seek(0)
        data = imgdata.getvalue()
        return data