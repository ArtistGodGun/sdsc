# SDSC - SingleDrumSourceClassification 
Hello. I am an "ArtistGodgun" (real name: Keonhee Hong) who studied composition in South Korea and has been involved in music activities across various genres. Currently, I am developing an artificial intelligence for music composition. 

## Project Description

This model is designed to classify various single-source sounds used in drums (such as kick, hi-hat, snare, etc.) when given an audio file input with a sample rate of 44.1 kHz and a bit depth of 16-bit. The audio file is converted to MFCC and trained using a simple CNN model commonly used for image classification. I created this model as a preliminary step to develop Multi Audio Source Classification, Drum Audio Separation, and Drum Transcription models.

## Classes
This model is currently able to distinguish between 10 classes or 16 classes.
```
# 10
'closed':0
'clap':1
'conga':2
'crash':3
'kick':4
'oh':5
'ride':6
'rim':7
'snare':8
'tom':9
```
```
# 16
'closed_a':0
'closed_e':1
'clap':2
'conga':3
'crash_a':4
'crash_e':5
'kick_ac':6
'kick_e':7
'oh_a':8
'oh_e':9
'ride':10
'ride_e':11
'rim':12
'snare':13
'snare_e':14
'tom':15
```

## Install
```
git clone https://github.com/ArtistGodGun/sdsc.git
cd ~/sdsc
python setup.py install
```

## Usage

This model takes the path of an audio file as input and returns the corresponding path and predicted class. If you need to organize your sample files in your audio folder, using this model could provide some assistance.

* Simple use
```
# Single files use (wav, mp3, ogg,...)
sdsc [test.wav]

# audio files path (After reading all the audio files in the folder, the results are exported.)
sdsc [path]
```

* command-line
```
# save to csv (y or n, default : n)
sdsc [path] -s y

# info print (y or n, default: y)
sdsc [path] -info y

# gpu device set (cpu or mps)
sdsc [path] -d mps # default : cpu

# model setting (10: 0, 16: 1)
sdsc [path] -m 0 # 10 class
sdsc [path] -m 1 # 16 class
```

## Dataset
The model distinguishes a total of 10 classes (Kick, Closed Hi-hat, Open Hi-hat, Snare, Clap, Crash, Ride, Rimshot, Conga, Tom) or 16 classes (kick_a, kick_e, closed_a, closed_e, open_a, open_e, ride, ride_e, crash_a, crash_e, clap, rimshot, snare_a, snare_e, tom, conga). For each class, 100 samples were used for training. The suffix "a" represents the acoustic genre, and "e" represents the EDM genre. Currently, there are two models trained: one with 10 classes and another with 16 classes. The goal is to expand the classes and integrate them into a single model using techniques such as ensemble learning. This approach was taken in order to achieve higher accuracy by first conducting the classification task with a smaller number of classes and then combining the fine-grained classes into common classes. Although it is not currently implemented, it is planned for future updates.

The length of each sample varies, but when inputted to the model, it is standardized to 1 second. For samples shorter than 1 second, they are padded with zeros to fit the 1-second length, and for samples longer than 1 second, they are trimmed to 1 second. No additional techniques like fade-out are used.

In the case of this model, more time and effort were invested in constructing the dataset rather than building the model itself. Many available samples in the dataset already contain mixed sources, such as combining hi-hat with kick for added attack or mixing snare and clap. Such samples were excluded as much as possible. The dataset was gathered from my personal collection of drum sources as well as from Splice.

I would like to share the dataset, but unfortunately, most of the data I used consists of commercially purchased samples, making it difficult to release the original data. I will explore the possibility of sharing the dataset by lowering the sample rate and consider releasing it in the future. If you can provide any assistance regarding this matter, please let me know via the email address at the bottom of this post. Thank you.

## Model
This is a simple CNN model that uses a stack of 2D Convolutional layers followed by Batch Normalization and ReLU activation. It then utilizes Fully Connected layers for classification. This is a common approach seen in image classification tasks. As the number of layers in the network increases, there is a tendency for the accuracy to improve. However, the quality and accuracy of the training data have a greater impact on the model's performance.


* The MFCC parameters used are:
```
n_fft = 4096
hop_length = 512
n_mels = 256
n_mfcc = 128
```

## Results
The accuracy of the test set ranges from 91% to 94%, on average. It often confuses similar drum types (such as Kick, Snare, and Tom) and metal types (such as Crash, Closed Hi-hat, Open Hi-hat, and Ride). I am currently researching ways to improve this.

## Limitations
Unfortunately, this model cannot distinguish between mixed sources in audio files. For example, it cannot determine whether it is a kick or a crash in an audio file that contains both. Additionally, it cannot predict sounds that are not in the task (such as voice, dog barking, piano, etc.).

## Contact Me
I am currently working on multi-source audio classification, drum source separation, and drum loop transcription research. You can find more details in a different repository. Please support me in these endeavors.
I am Korean and not fluent in English writing. Please note that this text is a translation generated by ChatGPT. 
Please send your inquiries to the email address (artistgodgun@gmail.com). When you send the email, please use simple English or Korean, and I will do my best to translate and read it. Thank you!