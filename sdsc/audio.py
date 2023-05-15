import torch, torchaudio
import torch.nn.functional as F

def resampleAudio(audio, sr):
    return torchaudio.transforms.Resample(sr, 44100)(audio)

def normalizeAsTorch(audio):
    return audio / torch.max(torch.abs(audio))

def audio_pad(audio, sr, duration = 1):
    if audio.size(0) == 2:
        audio = torch.mean(audio, dim=0).unsqueeze(0)
    length = int(duration * sr)
    padding = length - audio.size(1)
    if padding>0:
        audio = F.pad(audio, (0, padding), 'constant', 0)
    else:
        audio = audio[:, :length]
    return audio

def mfcc_torch(PATH):
    audio, sample_rate = torchaudio.load(PATH, normalize=True)
    if sample_rate != 44100:
        audio = resampleAudio(audio, sample_rate)
        sample_rate = 44100
    audio = audio_pad(audio, sample_rate)
    audio = normalizeAsTorch(audio)

    mfcc_transform = torchaudio.transforms.MFCC(sample_rate=sample_rate, n_mfcc=128, melkwargs={
        "n_fft": 4096,
        "hop_length" : 512,
        "n_mels" : 256,
        "center":True})
    return torch.nn.functional.normalize(mfcc_transform(audio))