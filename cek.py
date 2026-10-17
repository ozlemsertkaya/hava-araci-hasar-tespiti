import cv2, os, sys, csv
from datetime import datetime

if len(sys.argv) != 3:
    sys.exit('Kullanim: python cek.py N001 ezik   (sinif: saglam / catlak / ezik)')

numune, sinif = sys.argv[1], sys.argv[2]
if sinif not in ('saglam', 'catlak', 'ezik'):
    sys.exit('sinif saglam, catlak veya ezik olmali')

klasor = os.path.join('data', numune)
os.makedirs(klasor, exist_ok=True)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
if not cap.isOpened():
    sys.exit('Kamera acilamadi. VideoCapture(1) deneyin.')

print('BOSLUK: foto kaydet | Q: cik')
while True:
    ok, kare = cap.read()
    if not ok:
        break
    cv2.imshow('Onizleme', kare)
    tus = cv2.waitKey(1) & 0xFF
    if tus == ord(' '):
        n = len([f for f in os.listdir(klasor) if f.endswith('.jpg')]) + 1
        dosya = os.path.join(klasor, f'foto_{n:02d}.jpg')
        cv2.imwrite(dosya, kare)
        yeni = not os.path.exists('veri.csv')
        with open('veri.csv', 'a', newline='', encoding='utf-8') as f:
            w = csv.writer(f)
            if yeni:
                w.writerow(['dosya', 'sinif', 'numune_id', 'bolum', 'tarih'])
            w.writerow([dosya.replace(os.sep, '/'), sinif, numune, '', datetime.now().isoformat(timespec='seconds')])
        print('Kaydedildi:', dosya)
    elif tus == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()