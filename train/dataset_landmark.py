import torch
from torch.utils.data import Dataset

class LandMarkDataSet(Dataset):
    def __init__(self, csv_file:str):
        self.