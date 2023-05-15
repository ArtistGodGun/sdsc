import os
import csv
CLASSES =  {
    'closed':0, 'clap':1, 'conga':2,'crash':3,'kick':4,'oh':5,'ride':6,'rim':7,'snare':8,'tom':9
    }


def getPath(path):
    audio_list = []
    for root, dirs, files in os.walk(path):
        audio_files = [os.path.join(root, f) for f in files if f.endswith(('.wav', '.mp3'))]
        for i in audio_files:
            audio_list.append(i)
    return audio_list

def save_csv(save):
    with open('result.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for row in save:
            writer.writerow(row)
            
def print_info(info):
    for i in info:
        print(i)