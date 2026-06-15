{
  "train_batch_size": 4,
  "optimizer": {
    "type": "SGD",
    "params": {
      "lr": 0.001,
      "momentum": 0.9
    }
  },
  "fp16": {
    "enabled": true
  },
  "zero_optimization": {
    "stage": 2
  }
}

import deepseed
model_engine, optimizer, _, _ = deepspeed.initialize(args=cmd_args,
                                                      model=model,
                                                      model_parameters=params)

model_engine.save_checkpoint()
model_engine.load_checkpoint()





import torch
import torch.nn as nn
from torch.utils.data import TensorDataset, DataLoader
from accelerate import Accelerator, DeepSpeedPlugin

class TestNet(nn.Module):
    def __init__(self, input_dim: int, output_dim: int):
        super(TestNet, self).__init__()
        self.fc1 = nn.Linear(in_features=input_dim, out_features=output_dim)
        self.fc2 = nn.Linear(in_features=output_dim, out_features=output_dim)

    def forward(self, x: torch.Tensor):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

if __name__ == "__main__":
    input_dim = 8
    output_dim = 64
    batch_size = 8
    dataset_size = 1000
    input_data = torch.randn(dataset_size, input_dim)
    labels = torch.randn(dataset_size, output_dim)
    dataset = TensorDataset(input_data, labels)
    dataloader = DataLoader(dataset=dataset, batch_size=batch_size)

    model = TestNet(input_dim=input_dim, output_dim=output_dim)
    accelerator = Accelerator()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    loss_func = nn.MSELoss()

    model, optimizer, dataloader = accelerator.prepare(model, optimizer, dataloader)

    for epoch in range(10):
        model.train()
        for batch in dataloader:
            inputs, labels = batch
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = loss_func(outputs, labels)
            accelerator.backward(loss)
            optimizer.step()
        print(f"Epoch {epoch}, Loss: {loss.item()}")




+ from accelerate import Accelerator
+ accelerator = Accelerator()

+ model, optimizer, training_dataloader, scheduler = accelerator.prepare(
+     model, optimizer, training_dataloader, scheduler
+ )

  for batch in training_dataloader:
      optimizer.zero_grad()
      inputs, targets = batch
      inputs = inputs.to(device)
      targets = targets.to(device)
      outputs = model(inputs)
      loss = loss_function(outputs, targets)
+     accelerator.backward(loss)
      optimizer.step()
      scheduler.step()