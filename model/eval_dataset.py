import torch
from torch.utils.data import Dataset

class EvalDataset(Dataset):
    def __init__(self, data_array):
        self.data_array = data_array

    def __getitem__(self, idx) -> tuple:
        tensor_data = self.data_array
        tensor_data = torch.tensor(tensor_data)
        
        return tensor_data