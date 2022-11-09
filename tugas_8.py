from os import getpid
from time import time,sleep
from multiprocessing import cpu_count, Pool, Process

print ("Input Bilangan : ")
x = int(input())

def cetak(i):
	for i in range(x):
		if i % 2 == 0:
			print(f"angka ganjil-{i+1}"," - ID prosesnya ", getpid())
		else:
			print(f"angka genap-{i+1}"," - ID prosesnya ", getpid())
	sleep(1)

#Multiprocessing Sekuensial
print("Multiprocessing Sekuensial")
sekuensial_awal = time()

for i in range(1):
	cetak(i)
sekuensial_akhir = time()
print(" ")

#Multiprocessing Process
print("Multiprocessing Process")
kumpulan_proses = []
process_awal = time()

for i in range(1):
	p = Process(target=cetak, args=(i,))
	kumpulan_proses.append(p)
	p.start()
for i in kumpulan_proses:
	p.join()
process_akhir = time()
print(" ")

#Multiprocessing Pool
print("Multiprocessing Pool")
pool_awal = time()

pool = Pool()
pool.map(cetak, range(0,1))
pool.close()

pool_akhir = time()
print(" ")

#Banding Waktu Eksekusi
print("Sekuensial : ", sekuensial_akhir - sekuensial_awal, "detik")
print("Multiprocessing.Process : ", process_akhir - process_awal, "detik")
print("Multiprocessing.Pool : ", pool_akhir - pool_awal, "detik")

