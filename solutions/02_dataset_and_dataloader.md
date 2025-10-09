# Dataset and Dataloader

### Exercise 02.1

```python
training_data = datasets.MNIST(
    root="data",
    train=True,
    download=True,
    transform=v2.ToTensor()
)
labels_map = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
}
figure = plt.figure(figsize=(8, 8))
cols, rows = 3, 3
for i in range(1, cols * rows + 1):
    sample_idx = torch.randint(len(training_data), size=(1,)).item()
    img, label = training_data[sample_idx]
    figure.add_subplot(rows, cols, i)
    plt.title(labels_map[label])
    plt.axis("off")
    plt.imshow(img.squeeze(), cmap="gray")
plt.show()
```

### Exercise 02.2

```
len(training_data)
```
```
60000
```

Another approach is:

```
print(training_data)
Dataset MNIST
    Number of datapoints: 60000
    Root location: data
    Split: Train
    StandardTransform
Transform: ToTensor()
```

One could also do:

```
training_data.data.shape
```
```
(60000, 28, 28)
```

We see that there are 60000 samples in the training data for MNIST. Remember to use `dir(training_data)` to see the available methods and attributes.

There are 10000 samples in the test set.
