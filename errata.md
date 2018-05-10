## chapter 2
##　chapter 3
### 3.1.2
torch.FloatTensor(ndarray in float32) --- share memory
torch.FloatTensor(ndarray in float64) --- allocate new memory
### 3.2.2
saved_variables has been deleted in v0.3

### 5.1.1
- torchvision Scale -> Resize
- torchvision RandomSizedCrop -> RandomResizedCrop
- dataset collate_fn
  ```
  dataloader = DataLoader(dataset, 2, collate_fn=my_collate_fn, num_workers=1,shuffle=True)
  ```
### 5.4
module.cuda(device = 1) # device_id changed too

