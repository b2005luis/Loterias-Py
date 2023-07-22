from builtins import float

import torch
from torch import float
from torch.nn import Module, Linear, MSELoss, ReLU
from torch.optim import Adam
from torch.utils.data import DataLoader


class LoteriaNNTorch(Module):

    def __init__(self, input_size: int = 6, hidden_size: int = 60, output_size: int = 1):
        super(LoteriaNNTorch, self).__init__()
        self.relu = ReLU()
        self.hidden_layer = Linear(in_features=input_size, out_features=hidden_size)
        self.output_layer = Linear(in_features=hidden_size, out_features=output_size)

    def export_network(self, oath):
        torch.save(self.state_dict(), f"{oath}/state_netwirk")

    def forward(self, x):
        feature = self.hidden_layer(x)
        activation = self.relu(feature)
        output = self.output_layer(activation)
        return output

    def calibrate_loss(self, data_train, ephocs: int = 1000, target_loss=0.001):
        loader = DataLoader(dataset=data_train, batch_size=100, shuffle=True)

        criterion = MSELoss()
        optimizer = Adam(self.parameters(), lr=target_loss, weight_decay=0.009)

        for ix in range(ephocs):
            for i, data in enumerate(loader, 0):
                x_data, y_data = data

                optimizer.zero_grad()
                predict = self(x_data)
                current_loss = criterion(predict, y_data)

                print(f"Trenamento na fase {ix + 1} com perda de {current_loss}")

                current_loss.backward()
                optimizer.step()
