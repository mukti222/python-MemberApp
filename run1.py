#Run this prior to starting the exercise
from random import randint as rnd

memReg = '/members.txt'
exReg = '/inactive.txt'
fee =('yes','no')


def genFiles(current,old):
    with open(current,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
# current dan old, mewakili anggota aktif dan tidak aktif
# buka file yang diberikan dalam mode "w+" (write + read)
# {:^13}: kolom pertama (nomor keanggotaan) ^ rata tengah, 13 lebar kolom total karakter 
#{:<11} (tanggal bergabung). Tanda < isi akan diatur rata kiri
        for rowno in range(20):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date, fee[rnd(0,1)]))
# mengulangi proses 20 kali:
 # buat string tanggal acak(rnd = acak) format "YYYY-MM-DD".
 # Menghasilkan nomor keanggotaan acak antara 10000 dan 99999.
 # Memilih secara acak status keanggotaan ("yes" atau "no") dari tuple fee.
 # Menggabungkan semua data ini dengan format yang ditentukan dalam variabel data dan menulisnya ke dalam file.

    with open(old,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for rowno in range(3):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[1]))
#berisi file old inactive

genFiles(memReg,exReg)
# Pemanggilan ini akan memproses pembuatan dan pengisian kedua 
# file tersebut dengan data yang dihasilkan secara acak.
