import torch, torch.nn as nn
from torch.utils.data import DataLoader
from ortak import Veri, model_olustur

cihaz = 'cuda' if torch.cuda.is_available() else 'cpu'
egitim = DataLoader(Veri('veri.csv', 'egitim'), batch_size=16, shuffle=True)
dogrulama = DataLoader(Veri('veri.csv', 'dogrulama'), batch_size=16)

model = model_olustur()
for p in model.features.parameters():
    p.requires_grad = False
model = model.to(cihaz)

kayip = nn.CrossEntropyLoss()
opt = torch.optim.Adam(model.classifier.parameters(), lr=1e-3)

en_iyi = -1
for epoch in range(15):
    model.train()
    model.features.eval()
    for x, y in egitim:
        x, y = x.to(cihaz), y.to(cihaz)
        opt.zero_grad()
        kayip(model(x), y).backward()
        opt.step()

    model.eval()
    dogru = toplam = 0
    with torch.no_grad():
        for x, y in dogrulama:
            x, y = x.to(cihaz), y.to(cihaz)
            dogru += (model(x).argmax(1) == y).sum().item()
            toplam += len(y)
    acc = dogru / toplam
    print(f'epoch {epoch+1}  dogrulama dogruluk {acc:.2f}')
    if acc > en_iyi:
        en_iyi = acc
        torch.save(model.state_dict(), 'en_iyi.pt')