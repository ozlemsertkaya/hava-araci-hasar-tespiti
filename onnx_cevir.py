import torch
from ortak import model_olustur

model = model_olustur(on_egitimli=False)
model.load_state_dict(torch.load('en_iyi.pt', map_location='cpu'))
model.eval()
torch.onnx.export(model, torch.randn(1, 3, 224, 224), 'model.onnx')
print('model.onnx yazildi')