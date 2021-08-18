import numpy as np
import pandas as pd
import torch
from torch.utils.data import Dataset
from pathlib import Path


class NodulesDataset(Dataset):
    def __init__(
            self, nodules_folder: str, labels_file: str = "labels.csv", nodule_extension: str = ".npy", transform=None, return_path: bool = False
    ):
        self.return_path = return_path
        self.nodules = []
        self.labels = []
        self.paths = []
        labels_file = pd.read_csv(Path(nodules_folder).joinpath(labels_file))
        for _, row in labels_file.iterrows():
            self.paths.append(Path(nodules_folder).joinpath(f"{int(row['id'])}{nodule_extension}"))
            self.nodules.append(np.load(str(self.paths[-1])))
            self.labels.append(int(row["malignancy_th"]))
        self.nodules = np.array(self.nodules)
        self.labels = np.array(self.labels)
        self.transform = transform

    def __len__(self):
        return len(self.nodules)

    def __getitem__(self, idx: int):
        item = self.nodules[idx]
        label = self.labels[idx]
        if self.transform:
            item = self.transform(item)
        if self.return_path:
            return item, label, str(self.paths[idx])   
        else:
            return item, label
