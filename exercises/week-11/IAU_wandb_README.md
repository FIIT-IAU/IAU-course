```py
# -*- coding: utf-8 -*-
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
```

# Using Weights & Biases (wandb) to Log Training

#### Author: Sebastián Čambál (2024)

## Introduction

Weights & Biases (wandb) is a powerful tool for machine learning developers to track experiments, visualize data, and share insights with others. It's particularly useful for logging training processes, comparing different models, and optimizing model performance.

## Setting Up wandb

### Installation

To start using wandb, you need to install the wandb library. You can do this via pip:

```bash
pip install wandb
```

## Initialization

Before logging any data, you need to initialize wandb in your script:

```py
import wandb

# Log in to your W&B account
wandb.login()

# Initialize your W&B project
wandb.init(project='my_project_name', entity='my_entity_name')
```
- `wandb.login()` will prompt user for token found on the [website of your project](https://wandb.ai/site).
- `project`: Name of the project under which you'll group your experiments.
- `entity`: Your username or team name on wandb.

## Logging metrics

For logging you want to use `wandb.log()` and pass it a dict of values to log your metrics to wandb.

```py
# Example training loop
for epoch in range(epochs):
    for data, labels in train_loader:
        # Training process
        loss, accuracy = train(data, labels)
        
        # Log metrics
        wandb.log({"loss": loss, "accuracy": accuracy})
```

## Finishing Runs

To ensure that all data is properly synced and resources are released, use `wandb.finish()` at the end of your script or when you're done with a specific run:

```py
import wandb

wandb.login()
wandb.init(project='my_project_name', entity='my_entity_name')

for epoch in range(epochs):
    for data, labels in train_loader:
        loss, accuracy = train(data, labels)
        wandb.log({"loss": loss, "accuracy": accuracy})

# Finish the run to end the run and sync the logs
wandb.finish()
```

## Advanced Features

Logging configs and hyperparameters:

```py
config = dict(
    learning_rate = 0.01,
    epochs = 10,
    batch_size = 32
)

wandb.init(config=config)
```

Adding artifacts:

```py
artifact = wandb.Artifact('my-dataset', type='dataset')
artifact.add_file('my_dataset.csv')
wandb.log_artifact(artifact)
```
Hyperparameter sweeps:

```py
wandb.login()
wandb.init(...)

sweep_config = {
    'method': 'bayes',  # can be grid, random, or bayes
    'metric': {
        'name': 'loss',
        'goal': 'minimize'   
    },
    'parameters': {
        'learning_rate': {
            'min': 0.001,
            'max': 0.1
        },
        'epochs': {
            'values': [10, 20, 30]
        }
    }
}

sweep_id = wandb.sweep(sweep_config, project="my_project_name")
wandb.agent(sweep_id, function=train_function)
```
## Visualization and Analysis

After logging, you can visualize and analyze the results on the wandb dashboard. This includes plots for metrics, system health stats, and comparisons between different runs.
