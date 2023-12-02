import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from prettytable import PrettyTable

# Data dari Badan Pusat Statistik 
# https://www.bps.go.id/indicator/17/57/1/jumlah-kendaraan-bermotor.html

# Pemanggilan data menggunakan pandas
df = pd.read_csv('C:/VS Code/Projek TI/Jumlah_kendaraan_bermotor.csv')
df['Total'] = df[['2017', '2018', '2019', '2020', '2021']].sum(axis=1)
print (df)
tabel = PrettyTable(["Jenis Kendaraan Berdasarkan Jenis","2017", "2018", "2019", "2020", "2021"])

# tampilan pada matpplotlib
df.plot(x='Jenis Kendaraan Bermotor',y=['2017', '2018' , '2019', '2020', '2021'], kind='bar')
plt.title('Jumlah Kendaraan Bermotor per Jenis Kendaraan')
plt.xlabel('Jenis Kendaraan Bermotor')
plt.ylabel('Jumlah Kendaraan Bermotor (Juta)')
plt.xticks(rotation = 0)
plt.legend()
plt.show()
