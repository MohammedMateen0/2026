import torch
import torch.nn as nn
x=torch.rand(1,1,28,28)
pool=nn.MaxPool2d(kernel_size=2,stride=2)
output=pool(x)
print('Input shape:',x.shape)
print('Output shape:',output.shape)