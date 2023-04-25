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
	input(colored("Presione Enter para regresar: ", 'green'))
	os.system('clear')
	Appsistema()

def AppLista():
	print(colored("Cagando...", 'yellow'))
	time.sleep(0.5)
	os.system('clear')
	print(colored("Lista de perfiles", 'yellow'))
	print(colored("------------------------------------------", "blue", attrs=["bold"]))
	os.system('ls /etc/apparmor.d/')
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
	os.system('ls /usr/sbin/')
	print(colored("------------------------------------------", "blue", attrs=["bold"]))
	print(colored("Ingresa la ruta binaria del servicio", 'yellow'))
	print(colored("Plantilla: ", 'yellow'), "/usr/sbin/NombreDelServicio")
	print(colored("Ejemplo: ", 'yellow'), "/usr/sbin/mysqld")
	print("")
	print(colored("[r]", 'magenta'), "cancelar acción")
	print(colored("La ruta puede variar", 'magenta'))
	print(colored("------------------------------------------", "blue", attrs=["bold"]))
	perfilBinario = input(colored("Ruta del archivo binario del servicio: ", 'green'))
	
	if perfilBinario == "r":
		os.system('clear')
		menu()
	
	os.system('clear')
	
	if not os.path.exists(perfilBinario):
		print(colored("Parece que la ruta asignada no existe", 'red'))
		time.sleep(0.5)
		print(colored("La ruta asignada fue:", 'magenta'), perfilBinario)
		time.sleep(0.5)
		print(colored("------------------------------------------", "blue", attrs=["bold"]))
		input(colored("Pulse Enter para regresar: ", 'green'))
		AppPerfil()
	
	print(colored("Verifique que los datos sean correctos:", 'yellow'))
	print(colored("------------------------------------------", "blue", attrs=["bold"]))
	print("")
	print(colored("Ruta escrita: ", 'magenta') + perfilBinario)
	print("")
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
		os.system('systemctl reload apparmor.service')
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
	
	else:
		print(colored("Opción invalida", 'red'))
		time.sleep(1.5)
		os.system('clear')
		AppPerfil()
	

# ----------------------------------------------------------------------------------------

def Mseguro():
	os.system('ls /etc/apparmor.d/')
	print(colored("------------------------------------------", "blue", attrs=["bold"]))
	print(colored("Escriba el servicio que desea aplicar seguridad", 'yellow'))
	print(colored("Formato ejemplo:", 'yellow'), "usr.sbin.mysqld")
	print("")
	print(colored("[r]", 'magenta'), "cancelar acción")
	print("El formato no es permanente")
	print("puede variar de acuerdo al nombre del perfil asignato.")
	print(colored("------------------------------------------", "blue", attrs=["bold"]))
	servicio = input(colored("Servicio: ", 'green'))
	
	if servicio == "r":
		os.system('clear')
		AppAdmin()
	
	directorio = "/etc/apparmor.d/" + servicio
	os.system('clear')
	if not os.path.exists(directorio):
		print(colored("Parece que no existe ese perfil", 'red'))
		print(colored("------------------------------------------", "blue", attrs=["bold"]))
		time.sleep(0.5)
		print(colored("El dato de entrada fue:", 'yellow'), servicio)
		print(colored("La busqueda fue:", 'yellow'), directorio)
		print(colored("------------------------------------------", "blue", attrs=["bold"]))
		input(colored("Presione Enter para regresar: ", 'green'))
		os.system('clear')
		Mseguro()
	
	print(colored("Verifique que los datos sean correctos:", 'yellow'))
	print(colored("------------------------------------------", "blue", attrs=["bold"]))
	print("")
	print(colored("Perfil escrito: ", 'magenta') + servicio)
	print(colored("Directorio de busqueda: ", 'magenta') + directorio)
	print("")
	print("")
	print(colored("Desea continuar?:", 'yellow'), "[y/n]")
	print(colored("------------------------------------------", "blue", attrs=["bold"]))
	respuesta = input(colored("Respuesta: ", 'green'))
	os.system('clear')
	
	if respuesta == "y":
		print(colored("Aplicando seguridad...", 'yellow'))
		time.sleep(0.4)
		os.system('aa-enforce ' + servicio)
		os.system('systemctl reload apparmor.service')
		print(colored("------------------------------------------", "blue", attrs=["bold"]))
		time.sleep(0.4)
		os.system('apparmor_status')
		print(colored("------------------------------------------", "blue", attrs=["bold"]))
		time.sleep(0.4)
		print(colored("Verifique que se haya aplicado la seguridad", 'yellow'))
		print("")
		input(colored("Presione Enter para regresar al menu: ", 'green'))
		os.system('clear')
		AppAdmin()
	
	elif respuesta == "n":
		print(colored("Acción cancelada", 'red'))
		time.sleep(2)
		os.system('clear')
		AppAdmin()
	
	else:
		print(colored("Opción invalida", 'red'))
		time.sleep(2)
		os.system('clear')
		Mseguro()

	
def Mpermisivo():
	os.system('ls /etc/apparmor.d/')
	print(colored("------------------------------------------", "blue", attrs=["bold"]))
	print(colored("Escriba el perfil que desea poner en modo permisivo", 'yellow'))
	print(colored("Formato de ejemplo:"), "usr.sbin.mysqld")
	print("")
	print(colored("[r]", 'magenta'), "cancelar acción")
	print("El formato no es permanente")
	print("puede variar de acuerdo al nombre del perfil asignato.")
	print(colored("------------------------------------------", "blue", attrs=["bold"]))
	perfil = input(colored("Perfil: ", 'green'))
	
	if perfil == "r":
		os.system('clear')
		AppAdmin()
	
	directorio = "/etc/apparmor.d/" + perfil
	os.system('clear')
	
	if not os.path.exists(directorio):
		print(colored("Parece que no existe ese perfil", 'red'))
		print(colored("------------------------------------------", "blue", attrs=["bold"]))
		time.sleep(0.5)
		print(colored("El dato de entrada fue:", 'yellow'), perfil)
		print(colored("La busqueda fue:", 'yellow'), directorio)
		print(colored("------------------------------------------", "blue", attrs=["bold"]))
		input(colored("Presione Enter para regresar: ", 'green'))
		os.system('clear')
		Mpermisivo()
		
	print(colored("Verifique que los datos sean correctos:", 'yellow'))
	print(colored("------------------------------------------", "blue", attrs=["bold"]))
	print("")
	print(colored("Perfil escrito: ", 'magenta') + perfil)
	print(colored("Directorio de busqueda: ", 'magenta') + directorio)
	print("")
	print("")
	print(colored("Desea continuar?:", 'yellow'), "[y/n]")
	print(colored("------------------------------------------", "blue", attrs=["bold"]))
	respuesta = input(colored("Respuesta: ", 'green'))
	os.system('clear')
	
	if respuesta == "y":
		print(colored("Aplicando permicidad...", 'yellow'))
		time.sleep(0.4)
		os.system('aa-complain ' + directorio)
		os.system('systemctl reload apparmor.service')
		print(colored("------------------------------------------", "blue", attrs=["bold"]))
		time.sleep(0.4)
		os.system('apparmor_status')
		print(colored("------------------------------------------", "blue", attrs=["bold"]))
		time.sleep(0.4)
		print(colored("Verifique que se haya aplicado la permicidad", 'yellow'))
		print("")
		input(colored("Presione Enter para regresar al menu: ", 'green'))
		os.system('clear')
		AppAdmin()	
	
	elif respuesta == "n":
		print(colored("Acción cancelada", 'red'))
		time.sleep(2)
		os.system('clear')
		AppAdmin()
	
	else:
		print(colored("Opción invalida", 'red'))
		time.sleep(2)
		os.system('clear')
		Mpermisivo()
	
def AppDisable():
	os.system('ls /etc/apparmor.d/')
	print(colored("------------------------------------------", "blue", attrs=["bold"]))
	time.sleep(0.4)
	print(colored("Escriba el Perfil que desea deshabilitar", 'yellow'))
	print(colored("Formato: ", 'yellow'), "usr.sbin.mysqld")
	print("")
	print(colored("[r]", 'magenta'), "cancelar acción")
	print("El formato no es permanente")
	print("puede variar de acuerdo al nombre del perfil asignato.")
	print(colored("------------------------------------------", "blue", attrs=["bold"]))
	perfil = input(colored("Perfil: ", 'green'))
	
	if perfil == "r":
		os.system('clear')
		AppAdmin()
		
	directorio = "/etc/apparmor.d/" + perfil
	os.system('clear')
	
	if not os.path.exists(directorio):
		print(colored("Parece que no existe ese perfil", 'red'))
		print(colored("------------------------------------------", "blue", attrs=["bold"]))
		time.sleep(0.5)
		print(colored("El dato de entrada fue:", 'yellow'), perfil)
		print(colored("La busqueda fue:", 'yellow'), directorio)
		print(colored("------------------------------------------", "blue", attrs=["bold"]))
		input(colored("Presione Enter para regresar: ", 'green'))
		os.system('clear')
		AppDisable()
	
	print(colored("Verifique que los datos sean correctos:", 'yellow'))
	print(colored("------------------------------------------", "blue", attrs=["bold"]))
	print("")
	print(colored("Perfil escrito: ", 'magenta') + perfil)
	print(colored("Directorio de busqueda: ", 'magenta') + directorio)
	print("")
	print("")
	print(colored("Desea continuar con la desactivación?:", 'yellow'), "[y/n]")
	print(colored("------------------------------------------", "blue", attrs=["bold"]))
	respuesta = input(colored("Respuesta: ", 'green'))
	os.system('clear')
	
	if respuesta == "y":
		print(colored("Deshabilitando servicio", 'yellow'))
		time.sleep(0.4)
		os.system('aa-disable ' + directorio)
		os.system('systemctl reload apparmor.service')
		print(colored("------------------------------------------", "blue", attrs=["bold"]))
		time.sleep(0.4)
		os.system('apparmor_status')
		print(colored("------------------------------------------", "blue", attrs=["bold"]))
		time.sleep(0.4)
		print(colored("Verifique que se haya deshabilitado", 'yellow'))
		print("")
		input(colored("Presione Enter para regresar al menu: ", 'green'))
		os.system('clear')
		AppAdmin()	
	
	elif respuesta == "n":
		print(colored("Acción cancelada", 'red'))
		time.sleep(2)
		os.system('clear')
		AppAdmin()
	
	else:
		print(colored("Opción invalida", 'red'))
		time.sleep(2)
		os.system('clear')
		AppDisable()
			
	
def AppDelete():
	os.system('ls /etc/apparmor.d/')
	print(colored("------------------------------------------", "blue", attrs=["bold"]))
	time.sleep(0.4)
	print(colored("Escriba el Perfil que desea eliminar", 'yellow'))
	print(colored("Formato: ", 'yellow'), "usr.sbin.mysqld")
	print("")
	print(colored("[r]", 'magenta'), "cancelar acción")
	print("El formato no es permanente")
	print("puede variar de acuerdo al nombre del perfil asignato.")
	print(colored("------------------------------------------", "blue", attrs=["bold"]))
	perfil = input(colored("Perfil: ", 'green'))
	
	if perfil == "r":
		os.system('clear')
		AppAdmin()
		
	directorio = "/etc/apparmor.d/" + perfil
	os.system('clear')
	
	if not os.path.exists(directorio):
		print(colored("Parece que no existe ese perfil", 'red'))
		print(colored("------------------------------------------", "blue", attrs=["bold"]))
		time.sleep(0.5)
		print(colored("El dato de entrada fue:", 'yellow'), perfil)
		print(colored("La busqueda fue:", 'yellow'), directorio)
		print(colored("------------------------------------------", "blue", attrs=["bold"]))
		input(colored("Presione Enter para regresar: ", 'green'))
		os.system('clear')
		AppDelete()
	
	print(colored("Verifique que los datos sean correctos:", 'yellow'))
	print(colored("------------------------------------------", "blue", attrs=["bold"]))
	print("")
	print(colored("Perfil escrito: ", 'magenta') + perfil)
	print(colored("Directorio de busqueda: ", 'magenta') + directorio)
	print("")
	print("")
	print(colored("Desea continuar con la eliminación?:", 'yellow'), "[y/n]")
	print(colored("------------------------------------------", "blue", attrs=["bold"]))
	respuesta = input(colored("Respuesta: ", 'green'))
	os.system('clear')
	
	if respuesta == "y":
		print(colored("Eliminando perfil", 'yellow'))
		time.sleep(0.4)
		os.system('aa-disable ' + directorio)
		os.system('systemctl reload apparmor.service')
		time.sleep(0.4)
		os.system('rm ' + directorio)
		os.system('systemctl reload apparmor.service')
		print(colored("------------------------------------------", "blue", attrs=["bold"]))
		time.sleep(0.4)
		os.system('ls /etc/apparmor.d/')
		print(colored("------------------------------------------", "blue", attrs=["bold"]))
		time.sleep(0.4)
		print(colored("Verifique que se haya eliminado", 'yellow'))
		print("")
		input(colored("Presione Enter para regresar al menu: ", 'green'))
		os.system('clear')
		AppAdmin()	
	
	elif respuesta == "n":
		print(colored("Acción cancelada", 'red'))
		time.sleep(1.5)
		os.system('clear')
		AppAdmin()
	
	elif respuesta == "":
		print(colored("Acción denegada", 'red'))
		time.sleep("1.5")
		os.system('clear')
		AppDelete()
		
	elif respuesta == " ":
		print(colored("Acción denegada", 'red'))
		time.sleep("1.5")
		os.system('clear')
		AppDelete()		
	
	else:
		print(colored("Opción invalida", 'red'))
		time.sleep(1.5)
		os.system('clear')
		AppDelete()

def AppStatusPerfil():
	print(colored("Verificando status de perfiles...", 'yellow'))
	time.sleep(0.6)
	os.system('clear')
	print(colored("Status:", 'yellow'))
	print(colored("------------------------------------------", "blue", attrs=["bold"]))
	os.system("aa-status")
	print(colored("------------------------------------------", "blue", attrs=["bold"]))
	input(colored("Presione Enter para regresar: ", 'green'))
	os.system('clear')
	AppAdmin()
	

def AppAdmin():
	while True:
		print(colored("Menu de administración", 'magenta'))
		print(colored("------------------------------------------", "blue", attrs=["bold"]))
		print(colored("[1]", 'yellow'), "Asegurar un perfil")
		print(colored("[2]", 'yellow'), "Poner en permisivo un perfil")
		print(colored("---------------------------------", "yellow"))
		print(colored("[3]", 'yellow'), "Desactivar un perfil")
		print(colored("[4]", 'yellow'), "status de perfiles")
		print(colored("[5]", 'yellow'), "Borrar un perfil")
		print(colored("------------------------------------------", "blue", attrs=["bold"]))
		print(colored("╭──────────────────────────────╮", "red"))
		print(colored("│ ", 'red'), colored("[c] ", "magenta") + "limpiar  ", colored("[r]", "magenta"), "regresar", colored(" │", "red"))
		print(colored("│", 'red'), colored("        [0]", "magenta"),  "salir         " + colored("   │", "red"))
		print(colored("╰──────────────────────────────╯", "red"))
		opcion = input(colored("Seleccione una opción: ", 'green'))
		os.system('clear')
		
		if opcion == "1":
			Mseguro()
		elif opcion == "2":
			Mpermisivo()
		elif opcion == "3":
			AppDisable()
		elif opcion == "4":
			AppStatusPerfil()
		elif opcion == "5":
			AppDelete()
		elif opcion == "c":
			os.system('clear')
		elif opcion == "r":
			menu()
		elif opcion == "0":
			print(colored("Saliendo...", 'yellow', attrs=["bold"]))
			time.sleep(0.5)
			os.system('clear')
			sys.exit()
		else:
			print(colored("opción invalida", 'red'))
			time.sleep(1)
			os.system('clear')
			AppAdmin()

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
		print(colored("	      version - 1.3", attrs=["bold"]))
		print(colored("------------------------------------------", "blue", attrs=["bold"]))
		print(colored("[1]", 'yellow'), "Sistema")
		print(colored("[2]", 'yellow'), "Crear perfil")
		print(colored("[3]", 'yellow'), "Administrar perfiles")
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
		elif opcion == "3":
			AppAdmin()
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
