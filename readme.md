Hello, my name is ArtistGodgun (real name: Keonhee Hong) and I studied composition in South Korea. Currently, I am studying to develop an artificial intelligence model for music composition.

Project Description
This model is designed to classify various single-source sounds used in drums (such as kick, hi-hat, snare, etc.) when given an audio file input with a sample rate of 44.1 kHz and a bit depth of 16-bit. The audio file is converted to MFCC and trained using a simple CNN model commonly used for image classification. I created this model as a preliminary step to develop Drum Audio Separation and Drum Transcription models.

Dataset
The model distinguishes 10 classes (Kick, Closed Hi-hat, Open Hi-hat, Snare, Clap, Crash, Ride, Rimshot, Conga, Tom), with 100 samples used for each class. The length of each sample varies, but when inputted to the model, it is standardized to 1 second. For samples shorter than 1 second, it is padded with 0s, while for samples longer than 1 second, it is trimmed to 1 second. No additional techniques, such as fade-out, are used.

For this model, more time and effort were spent on constructing the dataset than on building the model itself. Most of the sources are divided into acoustic and EDM sources, and as much as possible, samples with mixed sources (such as mixing hi-hat with kick for attack or combining snare and clap) were excluded from the dataset. The dataset was gathered from my personal collection of drum sources as well as from Splice.

Model
The model uses the torchaudio MFCC to transform 1-second wave data into 2D Conv - BatchNorm - ReLU, stacked in five layers of a simple CNN model commonly used for image classification. The parameters used are:
n_fft = 4096
hop_length = 512
n_mels = 256
n_mfcc = 128
As the layers become deeper, the accuracy tends to increase, but it depends on how precise and accurate the training data is.

Results
The accuracy of the test set ranges from 91% to 94%, on average. It often confuses similar drum types (such as Kick, Snare, and Tom) and metal types (such as Crash, Closed Hi-hat, Open Hi-hat, and Ride). I am currently researching ways to improve this.

Limitations
Unfortunately, this model cannot distinguish between mixed sources in audio files. For example, it cannot determine whether it is a kick or a crash in an audio file that contains both. Additionally, it cannot predict sounds that are not in the task (such as voice, dog barking, piano, etc.).