#INVENTORY
import os.path

valPilihan = input("Input Data Inventory baru (ya/tidak)? ")
filedbinv = os.path.exists('db-inventory.txt')
if(filedbinv!=True):
  filenew = open('db-inventory.txt', 'w+')

while valPilihan.lower() =='ya':
  print('***********************************')
  valnamaPerangkat = input("Nama Perangkat: ")
  valLokasi = input("Lokasi: ")
  f = open("db-inventory.txt", "a")
  strtoSave = "Nama Perangkat: " + valnamaPerangkat +", "+"Lokasi: "+valLokasi
  # baris = [strtoSave]
  f.write(strtoSave+"\n")
  f.close()
  print('-----------------------------------')
  valPilihan = input("Input Data Inventory baru (ya/tidak)? ")

print('***********************************')
f = open("db-inventory.txt", "r")
print(f.read())