import os
import pyfiglet
from colorama import Fore, Style
from colorama import init
from sympy import *
import sympy as sy
#Para imprimir
from sympy.interactive.printing import init_printing
init_printing(use_unicode=False, wrap_line=False)
from sympy.matrices import Matrix, eye, zeros, ones, diag, GramSchmidt


#Funcion crea el banner de presentacion
def banner():
    ascii_banner = pyfiglet.figlet_format("Matriz")
    print(Fore.GREEN + ascii_banner)
    print(Fore.WHITE+"Elija la una opcion")
    print(Fore.GREEN)
    print("[1] Define una matriz")
    print("[2] Lista de matrices guardadas")
    print(Fore.YELLOW)
    print("\n[S] Salir | [L] Limpiar pantalla")
    print(Fore.WHITE)

class Switcher(object):
    def numero_del_metodo(self, argument):
        """Dispatch method"""
        nombre_metodo = 'metodo_' + str(argument)
        metodo = getattr(self, nombre_metodo, lambda: "Opcion no valida")
        # Call the method as we return it
        metodo()
    
    def metodo_1(self):
        M1=Matrix([[1, 2, 3], [-2, 0, 4]])
        print(M1)

    #Funcion para limpiar pantalla
    def metodo_L(self):
        #Para linux
        if os.name == "posix":
            os.system ("clear")
            banner()
        elif os.name == "ce" or os.name == "nt" or os.name == "dos":
            #Para Windows
            os.system ("cls")
            banner()

salir=False

banner()
while not salir:
    mtd=Switcher()#Instancia de la clase Switcher
    opc=input("-> ")
    mtd.numero_del_metodo(opc)
    
    if opc=="s":
        salir=True
    elif opc=="S":
        salir=True