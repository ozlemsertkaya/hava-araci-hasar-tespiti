# Hava Aracı Hasar Tespiti

Küçük metal sac numuneler üzerinde yüzey hasarını (çatlak benzeri çizgi, ezik)
kamera ve mesafe sensörüyle tespit eden prototip.

## Kurulum (Windows)
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
PyTorch: pytorch.org Get Started sayfasındaki komutla kurulur.

## Dosyalar
- kamera_test.py: kamera çalışıyor mu testi
- cek.py: numune fotoğrafı çeker ve veri.csv'ye kaydeder
- bol.py: eğitim, doğrulama ve test ayrımı (numune bazında, bir kez çalıştırılır)
- ortak.py, egit.py, test.py: model eğitimi ve değerlendirme
- onnx_cevir.py: modeli ONNX'e çevirir
- sahte_veri.py: prova için sahte veri üretir
- olcum_gurultu.py: mesafe sensörü gürültü testi
- vl53l0x_sensor/: Arduino kodu