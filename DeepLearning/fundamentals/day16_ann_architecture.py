import torch
import torch.nn as nn
import torch.nn.functional as F


class MedicalClassifierANN(nn.Module):

    def __init__(self, input_features: int, num_classes: int):
        super().__init__()

        self.fc1 = nn.Linear(input_features, 16)
        self.fc2 = nn.Linear(16, 8)
        self.fc3 = nn.Linear(8, num_classes)

    def forward(self, x):

        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)

        return x


# test run
model = MedicalClassifierANN(input_features=5, num_classes=3)

x = torch.rand(1,5)

output = model(x)

print(output)