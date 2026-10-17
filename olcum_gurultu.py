import serial, statistics

s = serial.Serial('COM3', 115200, timeout=2)   # port adini Arduino IDE'den bak
deger = []
while len(deger) < 100:
    satir = s.readline().decode(errors='ignore').strip()
    if satir.isdigit():
        deger.append(int(satir))
print('ortalama', statistics.mean(deger), 'std', statistics.stdev(deger))