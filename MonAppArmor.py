import itertools
import random
from datetime import datetime, timedelta
import sys
import os
from colorama import init
from termcolor import colored
import time

init()

print(colored("Cargando...", 'yellow'))
time.sleep(0.5)
os.system('clear')



# ----------------------------------------------------------------------------------------

def AppStatus():
	print(colored("Cargando...", 'yellow'))
	time.sleep(0.5)
	os.system('clear')
	print(colored("Para terminar status:", 'yellow'), colored("ctrl + c", 'red'))
	print(colored("------------------------------------------", "blue", attrs=["bold"]))
	os.system('sudo service apparmor status')
	print(colored("---------------------------------------", "blue", attrs=["bold"]))
	os.system('clear')
	Appsistema()

def AppLista():
	print(colored("Cagando...", 'yellow'))
	time.sleep(0.5)
	os.system('clear')
	print(colored("Lista de perfiles", 'yellow'))
	print(colored("------------------------------------------", "blue", attrs=["bold"]))
	os.system('apparmor_status')
	print(colored("------------------------------------------", "blue", attrs=["bold"]))
	input(colored("Precione Enter para regresar: ", 'green'))
	os.system('clear')
	Appsistema()



def Appsistema():
	while True:
		print(colored("Menu de sistema", 'magenta', attrs=["bold"]))
		print(colored("------------------------------------------", "blue", attrs=["bold"]))
		print(colored("[1]", 'yellow'), "Status del servicio")
		print(colored("[2]", 'yellow'), "Lista de perfiles")
		print(colored("------------------------------------------", "blue", attrs=["bold"]))
		print(colored("╭──────────────────────────────╮", "red"))
		print(colored("│ ", 'red'), colored("[c] ", "magenta") + "limpiar  ", colored("[r]", "magenta"), "regresar", colored(" │", "red"))
		print(colored("│", 'red'), colored("        [0]", "magenta"),  "salir         " + colored("   │", "red"))
		print(colored("╰──────────────────────────────╯", "red"))
		opcion = input(colored("selecciones una opcion: ", 'green'))
		os.system('clear')
		
		if opcion == "1":
			AppStatus()
		elif opcion == "2":
			AppLista()
		elif opcion == "c":
			os.system('clear')
		elif opcion == "r":
			os.system('clear')
			menu()
		elif opcion == "0":
			print(colored("Saliendo...", 'yellow'))
			time.sleep(0.5)
			os.system('clear')
			sys.exit()
		
		else:
			print(colored("Opción invalida", 'red'))
			time.sleep(1)
			os.system('clear')
			Appsistema()
		
# ----------------------------------------------------------------------------------------

def AppPerfil():
	print(colored("Ingresa la ruta binaria del servicio", 'yellow'))
	print(colored("Plantilla: ", 'yellow'), "/usr/sbin/NombreDelServicio")
	print(colored("Ejemplo: ", 'yellow'), "/usr/sbin/mysqld")
	print("")
	print(colored("La ruta puede variar", 'magenta'))
	print(colored("------------------------------------------", "blue", attrs=["bold"]))
	perfilBinario = input(colored("Ruta del archivo binario del servicio: ", 'green'))
	os.system('clear')
	print(colored("Verifique que los datos sean correctos:", 'yellow'))
	print(colored("------------------------------------------", "blue", attrs=["bold"]))
	print("")
	print("Ruta: " + perfilBinario)
	print("")
	print(colored("Desea continuar?:", 'yellow'), "[y/n]")
	print(colored("------------------------------------------", "blue", attrs=["bold"]))
	respuesta = input(colored("Respuesta: ", 'green'))
	os.system('clear')
	
	if respuesta == "y":
		print(colored("Creando perfil...", 'yellow'))
		time.sleep(0.4)
		print(colored("-------------------------------------------", "blue", attrs=["bold"]))
		os.system(f'sudo aa-genprof {perfilBinario}')
		print(colored("-------------------------------------------", "blue", attrs=["bold"]))
		print(colored("Operación realizada, verifique la creación:", 'yellow'))
		print(colored("-------------------------------------------", "blue", attrs=["bold"]))
		time.sleep(0.5)
		os.system('ls /etc/apparmor.d/')
		print(colored("-------------------------------------------", "blue", attrs=["bold"]))
		input(colored("Presione Enter para regresar: ", 'green'))
		os.system('clear')
		menu()
		
	
	elif respuesta == "n":
		print(colored("Acción cancelada", 'red'))
		time.sleep(1)
		os.system('clear')
		menu()


# ----------------------------------------------------------------------------------------


def menu():
	while True:
		print(colored('''
    _                  _                              
   / \   _ __  _ __   / \   _ __ _ __ ___   ___  _ __ 
  / _ \ | '_ \| '_ \ / _ \ | '__| '_ ` _ \ / _ \| '__|
 / ___ \| |_) | |_) / ___ \| |  | | | | | | (_) | |   
/_/   \_\ .__/| .__/_/   \_\_|  |_| |_| |_|\___/|_|   
        |_|   |_|
''', 'yellow', attrs=["bold"]))
		print(colored("	By Cañas", 'magenta', attrs=["bold"]))
		print(colored("	      version - 1", attrs=["bold"]))
		print(colored("------------------------------------------", "blue", attrs=["bold"]))
		print(colored("[1]", 'yellow'), "Sistema")
		print(colored("[2]", 'yellow'), "Crear perfil")
		print(colored("------------------------------------------", "blue", attrs=["bold"]))
		print(colored("╭──────────────────────────────╮", "red"))
		print(colored("│ ", 'red'), colored("[c] ", "magenta") + "limpiar  ", colored("[0]", "magenta"), "salir   ", colored(" │", "red"))
		print(colored("╰──────────────────────────────╯", "red"))

		opcion = input(colored("Seleccione una opción: ", "green"))
		os.system('clear')
		
		if opcion == "1":
			Appsistema()
		elif opcion == "2":
			AppPerfil()
		elif opcion == "c":
			os.system('clear')
		elif opcion == "0":
			print(colored("Saliendo...", 'yellow', attrs=["bold"]))
			time.sleep(0.5)
			os.system('clear')
			sys.exit()
		else:
			print(colored("Opción invalida", 'red'))
			time.sleep(1)
			os.system('clear')
			menu()

if __name__ == '__main__':
    menu()
