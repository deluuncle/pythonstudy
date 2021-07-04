import torch
import torchvision
import torchvision.transforms as transforms


train_set = torchvision.datasets.FashionMNIST(
    root='G:/data'
    ,train=True
    ,download=True
    ,transform=transforms.Compose([
        transforms.ToTensor()
    ])
)

images,lable = train_set[0]

print(images.shape)