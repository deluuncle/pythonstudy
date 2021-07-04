import torchvision
import torch
import torch.nn as nn
import torch.nn.functional as  F
import torchvision.transforms as transforms
import torch.optim as optim


class Network(nn.Module):
    def __init__(self):
        super(Network,self).__init__()
        self.conv1 = nn.Conv2d(in_channels=1,out_channels=6,kernel_size=5)
        self.conv2 = nn.Conv2d(in_channels=6,out_channels=12,kernel_size=5)

        self.fc1 = nn.Linear(in_features=12*4*4,out_features=120)
        self.fc2 = nn.Linear(in_features=120,out_features=60)
        self.out = nn.Linear(in_features=60,out_features=10)


    def forward(self,t):
        t = t

        t = self.conv1(t)
        t = F.relu(t)
        t = F.max_pool2d(t,kernel_size=2,stride=2)

        t = self.conv2(t)
        t = F.relu(t)
        t = F.max_pool2d(t,kernel_size=2,stride=2)

        t = t.reshape(-1,12*4*4)
        t = self.fc1(t)
        t = F.relu(t)

        t = self.fc2(t)
        t = F.relu(t)

        t = self.out(t)


        return t




N = Network()
train_set = torchvision.datasets.FashionMNIST(
    root='G:/data'
    ,train=True
    ,download=False
    ,transform=transforms.Compose([
        transforms.ToTensor()
    ])
)

train_loader = torch.utils.data.DataLoader(train_set,batch_size=100)
batch = next(iter(train_loader))
images,labels = batch


preds = N(images)
loss = F.cross_entropy(preds,labels)
print(loss.item())
print(N.conv1.weight.grad)
loss.backward()
print(N.conv1.weight.grad.shape)


optimizer = optim.SGD(N.parameters(),Ir=0.01)
loss.item()
get_num_correct(preds,labels)
optimizer.setup()

preds = N(images)
loss = F.cross_entropy(preds, labels)
loss.item()


get_num_correct(preds,labels)