import torch
x=torch.rand(5,5)
device='cuda' if tourc.cuda.is_available() else 'cpu'
x=x.to(device)
print('Tensor: ')
print(x)
print('Device: ',x.device)