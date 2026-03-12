# Deep Learning Foundations

This section introduces PyTorch and tensor operations.

## Day 14 – PyTorch Tensors

A tensor is a multi-dimensional array similar to a NumPy array but optimized for GPU computation.

Example:

```
torch.rand(5,5)
```

PyTorch tensor format for images:

```
(batch, channels, height, width)
```

Example:

```
(8, 3, 224, 224)
```

Where:

* 8 = batch size
* 3 = RGB channels
* 224 = image height
* 224 = image width
## Day 15 – PyTorch Autograd

PyTorch Autograd automatically computes gradients needed for training neural networks.

### Key Idea

When `requires_grad=True` is set on a tensor, PyTorch tracks all operations performed on it.

Calling `.backward()` computes gradients using automatic differentiation.

### Example

```python
import torch

x = torch.tensor([2.0,3.0])
w = torch.tensor([0.5,-0.2], requires_grad=True)

y = x * w
loss = y.sum()

loss.backward()

print(w.grad)
```

### Output

Gradients show how the loss changes with respect to the weights.

These gradients are later used by optimizers (like SGD or Adam) to update the model parameters.

