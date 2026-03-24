"""
Day 20 - Self Attention (Simplified)

Goal:
Understand attention mathematically, not just use libraries
"""

import torch
import torch.nn.functional as F

# Example input (sequence_length, embedding_dim)
X = torch.tensor([
    [1.0, 0.0, 1.0],
    [0.0, 2.0, 0.0],
    [1.0, 1.0, 0.0]
])

# Weight matrices
W_q = torch.rand(3, 3)
W_k = torch.rand(3, 3)
W_v = torch.rand(3, 3)

# Step 1: Compute Q, K, V
Q = X @ W_q
K = X @ W_k
V = X @ W_v

# Step 2: Compute attention scores
scores = Q @ K.T

# Step 3: Scale
d_k = K.shape[1]
scaled_scores = scores / (d_k ** 0.5)

# Step 4: Softmax
attention_weights = F.softmax(scaled_scores, dim=1)

# Step 5: Weighted sum
output = attention_weights @ V

print("Attention Weights:\n", attention_weights)
print("Output:\n", output)