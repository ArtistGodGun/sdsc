import glob
from torch.utils.data import Dataset
from .audio import mfcc_torch

class SDSDataset(Dataset):
    def __init__(self, path, onehot, combine):
        self.path = path
        self.classes = onehot
        self.combine = combine
        passClass = ['Brush', 'cowbell','kick_etc','snap','snare_trap','shaker','tambourine','timpani','triangle']
        self.filenames = glob.glob(f'{path}/*/*.wav')
        self.filenames = [f for f in self.filenames if f.split('/')[-2] not in passClass]
    def __len__(self):
        return len(self.filenames)
    def __getitem__(self, idx):
        file_path = self.filenames[idx]
        mfcc = mfcc_torch(file_path)
        if self.combine:
            label = self.classes[file_path.split('/')[-2].split('_')[0]]
        else:
            label = self.classes[file_path.split('/')[-2]]
        return mfcc, label, file_path