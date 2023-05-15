import os
import csv
CLASSES =  {
    'closed':0, 'clap':1, 'conga':2,'crash':3,'kick':4,'oh':5,'ride':6,'rim':7,'snare':8,'tom':9
    }


def getPath(path):
    audio_list = []
    for i in os.listdir(path):
        if i.endswith(('.wav', '.mp3')):
            audio_list.append(os.path.join(path,i))
    return audio_list

def save_csv(save):
    with open('result.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for row in save:
            writer.writerow(row)
            
def print_info(info):
    for i in info:
        print(i)