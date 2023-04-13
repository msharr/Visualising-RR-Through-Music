#Calculates RR peak ratios (N+1)/N
import numpy as np

class patientBar:
    def __init__(self, notes, tempo, start, end): 
        self.notes = notes
        self.tempo = tempo
        self.start = start
        self.end = end

def calculate_ratio(data, start_time):                     
    ratio = []
    ratio.append(patientBar(round(data[1]/data[0],4), round(60000/data[0]), start_time, start_time+(data[0]+data[1])/1000))
    for i in range(1,len(data)-1):                
        value = round(data[i+1]/data[i],4)
        ratio.append(patientBar(value, round(60000/data[i]), ratio[i-1].end, ratio[i-1].end+(data[i]+data[i+1])/1000))
        if i>15000:
            print("Limit reached: 15000 bars")
            break
    return ratio

def regions(ratio):
    a = 0
    b =0
    c=0
    d=0
    e=0
    f1=0
    g=0
    h=0
    j=0
    k=0
    l=0
    m=0
    for i in range(len(ratio)-1):
        if 0.35<=ratio[i].notes<0.45:
            ratio[i].notes = 0.4
            a = a +1
        elif 0.45<=ratio[i].notes<0.55:
            ratio[i].notes = 0.5
            b = b +1
        elif 0.55<=ratio[i].notes<0.675:
            ratio[i].notes = 0.66
            c = c+1
        elif 0.675<=ratio[i].notes<0.775:
            ratio[i].notes = 0.75
            d = d+1
        elif 0.775<=ratio[i].notes<0.9:
            ratio[i].notes = 0.8
            e = e+1
        elif 0.9<=ratio[i].notes<1.125:
            ratio[i].notes = 1
            f1=f1+1
        elif 1.125<=ratio[i].notes<1.29:
            ratio[i].notes = 1.25
            g=g+1
        elif 1.29<=ratio[i].notes<1.415:
            ratio[i].notes = 1.33
            h=h+1
        elif 1.415<=ratio[i].notes<1.625:
            ratio[i].notes = 1.5
            j = j+1
        elif 1.625<=ratio[i].notes<1.875:
            ratio[i].notes = 1.75
            k = k+1
        elif 1.875<=ratio[i].notes<2.25:
            ratio[i].notes = 2
            l = l+1
        elif 2.25<=ratio[i].notes:
            ratio[i].notes = 2.5
            m = m+1
    print(a,b,c,d,e,f1,g,h,j,k,l,m)
    return ratio

def main(patient_file, start_time):
    patient = np.loadtxt(patient_file)
    rr_ratio = calculate_ratio(patient, start_time) 
    patient_bars = regions(rr_ratio) 
    return patient_bars

if __name__ == "__main__":
    main()