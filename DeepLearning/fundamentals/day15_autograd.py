import torch
x=torch.tensor([2.0,3.0])
w=torch.tensor([0.5,-0.2],requires_grad=True)
y=x*w
loss=y.sum()
loss.backward()
print('Weight: ',w)
print('Gradients: ',w.grad)
