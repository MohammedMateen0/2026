"""
Day 19 - LSTM PyTorch Example
Minimal working example for sequence modeling
"""

import torch
import torch.nn as nn

# Define LSTM Model
class LSTMModel(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size):
        super(LSTMModel, self).__init__()
        
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)
    
    def forward(self, x):
        # Initialize hidden state and cell state
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size)
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size)
        
        # Forward propagate LSTM
        out, _ = self.lstm(x, (h0, c0))
        
        # Take output from last time step
        out = self.fc(out[:, -1, :])
        
        return out


if __name__ == "__main__":
    # Example input: (batch_size, sequence_length, input_size)
    x = torch.randn(2, 5, 3)
    
    model = LSTMModel(input_size=3, hidden_size=8, num_layers=1, output_size=1)
    
    output = model(x)
    print("Output shape:", output.shape)