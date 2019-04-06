#!/usr/bin/python
# Jika kamu ingin merecode code ini, donasi saya di "https://paypal.me/DonateTaufiq" thx :v
import time,os,sys

w = "\033[90;1m"
m = "\033[91;1m"
h = "\033[92;1m"
k = "\033[93;1m"
u = "\033[94;1m"
p = "\033[95;1m"
a = "\033[96;1m"
s = "\033[97;1m"

logo = '''
\t\t############################################
\t\t#\033[91;1m Autor  =\033[96;1m  Taufiq Stark\033[92;1m                   #
\t\t#\033[91;1m Github =\033[96;1m  https://github.com/TaufiqStark\033[92;1m #
\t\t#\033[91;1m Donasi =\033[96;1m  https://paypal.me/DonateTaufiq\033[92;1m #
\t\t############################################  
'''
lagi = 'y'
while lagi == 'y':
	print(u)
	os.system('figlet Perkiraan Cuaca !')
	print(h,logo,p)
	print('Jika baru pake silahkan install alatnya dulu dan\njangan lupa nyalakan data / WiFi anda!')
	print(h)
	print(s+'1)'+h+' Cek Cuaca\n'+s+'2)'+h+' Install alatnya dulu\n'+s+'3)'+h+' Exit\n')
	pil = int(input('Masukkan angka: '+a))
	
	def Cek():
		print(u)
		kota = input('Tuliskan Nama Kota: '+a)
		print('Waiting....')
		time.sleep(2)
		print(h)
		os.system('curl http://wttr.in/{}'.format(kota))
		print(m+'\n*Cubit layar anda agar terlihat lebih jelas')
		
		
	def Installl():
		os.system('pkg update && pkg upgrade -y')
		os.system('pkg install figlet -y')
		os.system('clear')
		os.system('pkg install curl -y')
		os.system('clear')
	def Exit():
		sys.exit(1)
	
	if pil == 1:
		Cek()
		lagi = input(h+'\nLagi??[y/n]: '+a)
	if pil == 2:
		Installl()
	if pil == 3:
		Exit()
	