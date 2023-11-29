import pandas as pd
import matplotlib.pyplot as plt

# Data dari badan pusat statistik 
# https://www.bps.go.id/indicator/17/57/1/jumlah-kendaraan-bermotor.html
df = pd.read_csv('C:/VS Code/Projek TI/Jumlah_kendaraan_bermotor.csv')

# Tampilan grafik bar matplotlib
fig, ax = plt.subplots(figsize=(10, 5))
df.plot('Jenis Kendaraan Bermotor',['2017', '2018' , '2019', '2020', '2021'], kind ='bar',ax=ax)
ax.set_title('Jumlah Kendaraan Bermotor per Jenis Kendaraan')
ax.set_xlabel('Jenis Kendaraan Bermotor')
ax.set_ylabel('Jumlah Kendaraan Bermotor (Ratusan Ribu)')
plt.xticks(rotation=0)

# Memunculkan Grafik
plt.show()