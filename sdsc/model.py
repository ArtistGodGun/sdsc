from torch import nn

class SDSClassification(nn.Module):
    def __init__(self, classes):
        super(SDSClassification,self).__init__()
        num_classes = len(classes)
        
        self.conv = nn.Sequential(
            nn.Conv2d(in_channels=1, out_channels=20, kernel_size=3, stride=2, padding=1),
            nn.BatchNorm2d(20),
            nn.ReLU(True),
            nn.Conv2d(in_channels=20, out_channels=40, kernel_size=3, stride=2, padding=1),
            nn.BatchNorm2d(40),
            nn.ReLU(True),
            nn.Conv2d(in_channels=40, out_channels=100, kernel_size=3, stride=2, padding=1),
            nn.BatchNorm2d(100),
            nn.ReLU(True),
            nn.Conv2d(in_channels=100, out_channels=200, kernel_size=3, stride=2, padding=1),
            nn.BatchNorm2d(200),
            nn.ReLU(True),
            nn.Conv2d(in_channels=200, out_channels=400, kernel_size=3, stride=2, padding=1),
            nn.BatchNorm2d(400),
            nn.ReLU(True),
        )
        self.fc = nn.Sequential(
            nn.Linear(400*4*3, 500),
            nn.ReLU(True),
            nn.Linear(500, 500),
            nn.ReLU(True),
            nn.Linear(500, num_classes),
        )
    def forward(self, x):
        x = self.conv(x)
        # print(x.size())
        x = x.view(-1, 400*4*3)
        x = self.fc(x)
        return x

