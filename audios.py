import wave 
import os, glob
from pathlib import Path
import csv
from itertools import zip_longest
from matplotlib import pyplot as plt
import sys
import soundfile as sf


def audiofiles(path,c,bins):
    if(path=='.'):
        path=os.getcwd()
    duration_list=[]
    filename_list=[]
    samplingrate_list=[]
    
    for filename in glob.glob(os.path.join(path, '*.wav')):
        data, samplerate = sf.read(filename)
        print(filename)
        
        sf.write('file-2.wav', data, samplerate, subtype='PCM_16')
        #sf.write(filename, data, samplerate, subtype='PCM_16')
        
        w = wave.open('file-2.wav', 'r')
        filename_list.append(Path(filename).stem)
        frames = w.getnframes()
        rate = w.getframerate()
        
        duration = frames / float(rate)
        duration_list.append(duration)
        samplingrate_list.append(rate)
        os.remove('file-2.wav')
        w.close()
    
    if(c=='.'):
        saveAddr=os.getcwd()+'/audio-information.csv' 
    else:    
        saveAddr=c+'/audio-information.csv'   
    generate_csv_file(saveAddr,filename_list,duration_list,samplingrate_list)
    generate_histogram(duration_list,bins)

def generate_csv_file(saveAddr,filename_list,duration_list,samplingrate_list):
    data = [filename_list,duration_list,samplingrate_list]
    export_data = zip_longest(*data, fillvalue = '')
    with open(saveAddr, 'w', encoding="ISO-8859-1", newline='') as file:
      write = csv.writer(file)
      write.writerow(("File Name", "Duration","Sampling Rate"))
      write.writerows(export_data)


def generate_histogram(duration_list,bin):
    plt. hist(duration_list,bins= int(bin))
    plt.xlabel("Duration")
    plt.ylabel("Frequency")
    plt.show()
    
if __name__=='__main__':
    audiofiles(sys.argv[1],sys.argv[2],sys.argv[3])
   
    
     
