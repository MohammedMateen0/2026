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
