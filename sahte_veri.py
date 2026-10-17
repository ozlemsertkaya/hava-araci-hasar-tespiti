import os, csv
import numpy as np
from PIL import Image

os.makedirs('data', exist_ok=True)
with open('veri.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['dosya', 'sinif', 'numune_id', 'bolum', 'tarih'])
    for i in range(30):
        sinif = ['saglam', 'catlak', 'ezik'][i % 3]
        nid = f'S{i:03d}'
        os.makedirs(f'data/{nid}', exist_ok=True)
        for k in range(3):
            arr = (np.random.rand(224, 224, 3) * 255).astype('uint8')
            yol = f'data/{nid}/foto_{k+1:02d}.jpg'
            Image.fromarray(arr).save(yol)
            w.writerow([yol, sinif, nid, '', ''])