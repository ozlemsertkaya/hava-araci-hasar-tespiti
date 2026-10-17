import sys
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('veri.csv')
if df['bolum'].notna().any():
    sys.exit('bolum zaten dolu. Test ayrimi bir kez yapilir, tekrar calistirma.')

def ana_sinif(s):
    kusur = [x for x in s if x != 'saglam']
    return kusur[0] if kusur else 'saglam'

numune = df.groupby('numune_id')['sinif'].apply(ana_sinif).reset_index()
egit_dog, test = train_test_split(numune, test_size=0.3, stratify=numune['sinif'], random_state=42)
egit, dog = train_test_split(egit_dog, test_size=0.2, stratify=egit_dog['sinif'], random_state=42)

bolum = {}
for n in egit['numune_id']: bolum[n] = 'egitim'
for n in dog['numune_id']: bolum[n] = 'dogrulama'
for n in test['numune_id']: bolum[n] = 'test'
df['bolum'] = df['numune_id'].map(bolum)
df.to_csv('veri.csv', index=False)
print(df.groupby(['bolum', 'sinif']).size())