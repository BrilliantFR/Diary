## Penyederhanaan command
# first_name = 'joseph'
# last_name = 'choi'
# full_name = f'{first_name} {last_name}'
# print(full_name)

## Library untuk tanggal
from datetime import datetime
today = datetime.now()
#or add
date_time = today.strftime("%Y-%m-%d %H:%M:%S") #format yang digunakan bebas, bisa pakai - semua
print(today)