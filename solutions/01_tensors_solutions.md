# Tensors

### Exercise 01.1
```
mytensor = torch.tensor([[2.1, -8.3, 3.5], [4.0, 5.9, 6.1], [-7.3, 8.0, 2.4]])
mytensor.device
```
```
device(type='cpu')
```

Move it to the GPU:

```
mytensor.to(torch.accelerator.current_accelerator())
```

### Exercise 01.2

```
torch.linalg.inv(mytensor)
```
```
tensor([[-0.0542,  0.0750, -0.1115],
        [-0.0847,  0.0479,  0.0019],
        [ 0.1174,  0.0685,  0.0713]])
```
