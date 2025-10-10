The Normalize transform normalizes the data to have a mean of 0 and standard deviation of 1.

```
Normalize((0.1307,), (0.3081,))
```

The mean is 0.1307 and the standard deviation is 0.381.

When using a pre-trained model is it important to know how the input data should be transformed before passing it through the model.

Run the lines below to see where the mean and standard deviation are coming from:

```
ds.data.numpy().mean()/255
ds.data.numpy().std()/255
```
