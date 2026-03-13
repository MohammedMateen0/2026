import torch
import torch.nn as nn
import torch.optim as optim


class MedicalClassifierANN(nn.Module):

    def __init__(self, input_features, num_classes):
        super().__init__()

        self.fc1 = nn.Linear(input_features, 16)
        self.fc2 = nn.Linear(16, 8)
        self.fc3 = nn.Linear(8, num_classes)

    def forward(self, x):

        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)

        return x


# dummy dataset
X_train = torch.rand(10, 5)
y_train = torch.randint(0, 3, (10,))


model = MedicalClassifierANN(5, 3)

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)


for epoch in range(50):

    model.train()

    predictions = model(X_train)

    loss = criterion(predictions, y_train)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 10 == 0:
        print(f"Epoch {epoch} Loss {loss.item()}")