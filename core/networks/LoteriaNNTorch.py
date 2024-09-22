import torch
from torch import Tensor
from torch.nn import Module, Linear, ReLU, MSELoss, LeakyReLU
from torch.optim import Adam, SGD
from torch.utils.data import DataLoader


class LoteriaNNTorch(Module):

    def __init__(self, input_size: int = 6, hidden_size: int = 60, output_size: int = 1, layers: int = 4):
        super(LoteriaNNTorch, self).__init__()
        self.layers = layers
        self.relu = LeakyReLU()
        self.hidden_layer = Linear(in_features=input_size, out_features=hidden_size)
        self.output_layer = Linear(in_features=hidden_size, out_features=output_size)

    def export_network(self, oath):
        torch.save(self.state_dict(), f"{oath}/state_network")

    def forward(self, x):
        output = None
        for l in range(self.layers):
            feature = self.hidden_layer(x)
            activation = self.relu(feature)
            output = self.output_layer(activation)
        return output

    def calibrate_loss(self, data_train, ephocs: int = 1000, learnung_rate=1e-1, decay=1e-5):
        loader = DataLoader(dataset=data_train, batch_size=500, shuffle=True)
        criterion = MSELoss()
        optimizer = SGD(self.parameters(), lr=learnung_rate, weight_decay=decay)

        for ix in range(ephocs):
            for i, data in enumerate(loader, 0):
                x_data, y_data = data

                predict = self(x_data)
                current_loss: Tensor = criterion(predict, y_data)

                print(f"Época: {ix}")
                print(f"Loss: {current_loss:.3f}")

                if (predict[0] / y_data[0]) < 0.5:
                    optimizer.zero_grad()
                    current_loss.backward()
                    optimizer.step()
                    print("*** Otimizado!")

