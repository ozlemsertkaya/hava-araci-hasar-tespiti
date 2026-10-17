import time, torch
from sklearn.metrics import classification_report, confusion_matrix
from torch.utils.data import DataLoader
from ortak import Veri, SINIFLAR, model_olustur

cihaz = 'cuda' if torch.cuda.is_available() else 'cpu'
model = model_olustur(on_egitimli=False)
model.load_state_dict(torch.load('en_iyi.pt', map_location=cihaz))
model.to(cihaz).eval()

yukleyici = DataLoader(Veri('veri.csv', 'test'), batch_size=16)
gercek, tahmin = [], []
t0 = time.time()
with torch.no_grad():
    for x, y in yukleyici:
        tahmin += model(x.to(cihaz)).argmax(1).cpu().tolist()
        gercek += y.tolist()
sure = (time.time() - t0) / len(gercek)

print(classification_report(gercek, tahmin, labels=[0, 1, 2], target_names=SINIFLAR, zero_division=0))
print(confusion_matrix(gercek, tahmin, labels=[0, 1, 2]))
print(f'Foto basina ortalama sure: {sure:.3f} sn (dosya okuma dahil)')