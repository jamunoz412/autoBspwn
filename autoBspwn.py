#!/usr/bin/python3

import signal, time, os
from sys import stdout

def red():
    RED = "\033[1;31m"
    stdout.write(RED)

def blue():
    BLUE = "\033[1;34m"
    stdout.write(BLUE)

def def_handler(sig, frame):
	print("\n\n[!] Saliendo...\n")
	sys.exit(1)


#Ctlr + C
signal.signal(signal.SIGINT,def_handler)

# variables globales

banner = """s             _        ____
  __ _ _   _| |_ ___ | __ ) ___ _ ____      ___ __  
 / _` | | | | __/ _ \|  _ \/ __| '_ \ \ /\ / / '_ \ 
| (_| | |_| | || (_) | |_) \__ \ |_) \ V  V /| | | |  (by j4munoff)
 \__,_|\__,_|\__\___/|____/|___/ .__/ \_/\_/ |_| |_|
                               |_|                  
"""

# Instalamos sublime-text, code y kitty
def programas_previos():

	blue()
	print("  [1] Instalando programas previos ....\n")
	os.system("sudo rm ~/firefox.tar.bz2 > /dev/null 2>&1")
	os.system("wget -O ~/firefox.tar.bz2  'https://download.mozilla.org/?product=firefox-latest&os=linux64&lang=es-ES'")
	os.system("sudo mv ~/firefox.tar.bz2 /opt")
	os.system("sudo tar -xf /opt/firefox.tar.bz2 -C /opt")
	os.system("sudo rm /opt/firefox.tar.bz2")
	os.system("rm -r ~/.mozilla > /dev/null 2>&1")
	os.system("cp -r ./config/mozilla ~/.mozilla > /dev/null 2>&1")
	os.system("sudo apt update")
	os.system("sudo parrot-upgrade")
	os.system('sudo apt install apt-transport-https ')
	os.system('wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -')
	os.system('echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list')
	os.system('curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg ')
	os.system('sudo mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg ')
	os.system('echo "deb [arch=amd64] http://packages.microsoft.com/repos/vscode stable main" | sudo tee /etc/apt/sources.list.d/vs-code.list')
	os.system('sudo apt update')
	os.system('sudo apt install sublime-text code kitty')
	blue()
	print("\n  [1] Instalados programas previos.\n")


def menu():


	red()
	print(banner)
	blue()
	print("\n\n Iniciando instalación\n")

	programas_previos()

	print("\n Instalación finalizada\n")

def executeCommand():


	menu()

if __name__ == "__main__":

	executeCommand()