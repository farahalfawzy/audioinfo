import wave 
import os, glob
from pathlib import Path
import csv
from itertools import zip_longest
from matplotlib import pyplot as plt
import sys

duration_list=[]
filename_list=[]
samplingrate_list=[]

    


def audiofiles(path,c):
    
    if(path=='.'):
        path=os.getcwd()
 
    for filename in glob.glob(os.path.join(path, '*.wav')):
        w = wave.open(filename, 'r')
        filename_list.append(Path(filename).stem)
        frames = w.getnframes()
        rate = w.getframerate()
        duration = frames / float(rate)
        duration_list.append(duration)
        samplingrate_list.append(rate)
        w.close()

    if(c=='.'):
        saveAddr=os.getcwd()+'/audio-information.csv' 
    else:    
        saveAddr=c+'/audio-information.csv'   
    generate_csv_file(saveAddr)
    generate_histogram()

def generate_csv_file(saveAddr):
    data = [filename_list,duration_list,samplingrate_list]
    export_data = zip_longest(*data, fillvalue = '')
    with open(saveAddr, 'w', encoding="ISO-8859-1", newline='') as file:
      write = csv.writer(file)
      write.writerow(("File Name", "Duration","Sampling Rate"))
      write.writerows(export_data)


def  generate_histogram():
    plt. hist(duration_list)
    plt.xlabel("Duration")
    plt.ylabel("Frequency")
    plt.show()

audiofiles(sys.argv[1],sys.argv[2])  
     
