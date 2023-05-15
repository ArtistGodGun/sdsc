import SDSCDataset
import torch
from torch.utils.data import DataLoader, random_split
from torch import nn, optim
from model import SDSClassification

# random.seed(1000)
# torch.manual_seed(1000)
path = '/Users/hongair/Desktop/develope/PYTHON/rein/Source'
combine = False
if combine:
    onehot = {'closed':0, 'clap':1, 'conga':2,'crash':3,'kick':4,'oh':5,'ride':6,'rim':7,'snare':8,'tom':9}
    # onehot = {'closed':0, 'clap':1, 'conga':2,'crash':3,'kick':4,'oh':5,'ride':6,'rim':7,'snare':8,'tom':9, 'Brush':10, 'cowbell':11, 'snap': 12, 
    # 'shaker': 13, 'tambourine':14, 'timpani':15, 'triangle':16}
else:
    onehot = {'closed_a':0, 'closed_e':1, 'clap':2, 'conga':3,'crash_a':4,'crash_e':5,'kick_ac':6,'kick_e':7,'oh_a':8,'oh_e':9,'ride':10,'ride_e':11,'rim':12,'snare':13,'snare_e':14,'tom':15}
    # onehot = {
    #     'closed_a':0, 'closed_e':1, 'clap':2, 'conga':3,'crash_a':4,
    #     'crash_e':5,'kick_ac':6,'kick_e':7,'oh_a':8,'oh_e':9,
    #     'ride':10,'ride_e':11,'rim':12,'snare':13,'snare_e':14,'tom':15,
    #     'Brush':16, 'cowbell':17, 'kick_etc':18, 'snap': 19, 'snare_trap':20,
    #     'shaker': 21, 'tambourine':22, 'timpani':23, 'triangle':24
    #     }

convert_onehot = {v:k for k,v in onehot.items()}

BATCH = 100
device = 'mps'
learning_rate = 1e-4
EPOCH = 500
dataset = SDSCDataset.SDSDataset(path, onehot, combine)
dataset_size = len(dataset)
train_size = int(dataset_size * 0.8)
test_size = dataset_size - train_size
train_dataset, test_dataset = random_split(dataset, [train_size, test_size])

train_dataloader = DataLoader(train_dataset, batch_size = BATCH, shuffle=True)
test_dataloader = DataLoader(dataset, batch_size=BATCH, shuffle=True)
print(f'Train : {len(train_dataloader)}, TEST: {len(test_dataloader)}, CLASSES : {len(onehot)}')
criterion = nn.CrossEntropyLoss()
model = SDSClassification(onehot).to(device)
# if 'model.pth' in os.listdir():
#     model.load_state_dict(torch.load('model.pth'))
optimizer = optim.Adam(model.parameters(), lr = learning_rate)
scheduler = torch.optim.lr_scheduler.MultiplicativeLR(optimizer=optimizer,lr_lambda= lambda epoch: 0.99 ** epoch)

model.train()
for epoch in range(EPOCH):
    total_loss = []
    for data, target, path in train_dataloader:
        data, target= data.to(device), target.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        total_loss.append(loss.item())
        loss.backward()
        optimizer.step()
    print(f'EPOCH : {epoch}, LOSS : {torch.mean(torch.Tensor(total_loss)).item()}')
    if (epoch + 1) %20 == 0:
        scheduler.step()
torch.save(model.state_dict(), f'sdsc_{len(onehot)}.pth')
model.load_state_dict(torch.load(f'sdsc_{len(onehot)}.pth'))
model.eval()
test_loss = 0
correct = 0

class_corect = list(0. for i in range(len(onehot)))
class_total = list(0. for i in range(len(onehot)))

l = []
p = []
see = []
with torch.no_grad():
    for data, target, name in test_dataloader:
        data, target = data.to(device), target.to(device)
        output = model(data)
        test_loss += criterion(output, target).item()
        _,pred = torch.max(output.data, 1)
        c = (pred == target).squeeze()
        for j in range(data.size(0)):
            l.append(target[j].item())
            p.append(pred[j].item())
            label = target[j]
            class_corect[label] += c[j].item()
            class_total[label] +=1
            if target[j].item() != pred[j].item():
                see.append([name[j], convert_onehot[target[j].item()], convert_onehot[pred[j].item()]])
            else:
                correct +=1


# for i in range(len(onehot)):
#     print('Accuracy of {}: {}% {}/{}'.format(convert_onehot[i], 100 * class_corect[i]/class_total[i], class_corect[i],class_total[i]))
for i in see:
    print(i)
print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
        test_loss, correct, len(test_dataloader.dataset),
        100. * correct / len(test_dataloader.dataset)))
# cm = confusion_matrix(l, p)
# plot_confusion_matrix(cm, labels=list(convert_onehot.values()), normalize=True)
