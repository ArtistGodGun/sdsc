import torch
import pkg_resources
from .model import SDSClassification
from .audio import mfcc_torch

def eval(path, device, combine):
    if combine:
        onehot = {'closed':0, 'clap':1, 'conga':2,'crash':3,'kick':4,'oh':5,'ride':6,'rim':7,'snare':8,'tom':9}
    else:
        onehot = {'closed_a':0, 'closed_e':1, 'clap':2, 'conga':3,'crash_a':4,'crash_e':5,'kick_ac':6,'kick_e':7,'oh_a':8,'oh_e':9,'ride':10,'ride_e':11,'rim':12,'snare':13,'snare_e':14,'tom':15}
    convert_onehot = {v:k for k,v in onehot.items()}
    model = SDSClassification(onehot)
    p = pkg_resources.resource_filename('sdsc', f'sdsc_{len(onehot)}.pth')
    if device == 'cpu':
        model.load_state_dict(torch.load(p, map_location=device))
    else:
        model.load_state_dict(torch.load(p)).to(device)
    model.eval()
    return_list = []
    with torch.no_grad():
        for i in path:
            mfcc = mfcc_torch(i).unsqueeze(0).to(device)
            output = model(mfcc)
            return_list.append((i, convert_onehot[torch.max(output.data,1)[1].item()]))
    return return_list