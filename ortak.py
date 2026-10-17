import pandas as pd
import torch.nn as nn
from PIL import Image
from torch.utils.data import Dataset
from torchvision import models, transforms

SINIFLAR = ['saglam', 'catlak', 'ezik']

donusum = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
])

class Veri(Dataset):
    def __init__(self, csv, bolum):
        df = pd.read_csv(csv)
        self.df = df[df['bolum'] == bolum].reset_index(drop=True)
    def __len__(self):
        return len(self.df)
    def __getitem__(self, i):
        s = self.df.iloc[i]
        img = Image.open(s['dosya']).convert('RGB')
        return donusum(img), SINIFLAR.index(s['sinif'])

def model_olustur(on_egitimli=True):
    agirlik = models.MobileNet_V3_Small_Weights.DEFAULT if on_egitimli else None
    model = models.mobilenet_v3_small(weights=agirlik)
    model.classifier[3] = nn.Linear(model.classifier[3].in_features, len(SINIFLAR))
    return model