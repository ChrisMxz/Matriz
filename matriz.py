from ast import parse
import os
from numpy.lib.function_base import append
import pyfiglet
from colorama import Fore, Style
from colorama import init
from sympy import *
import sympy as sy
import numpy as np 
from typing import OrderedDict
from sympy.interactive.printing import NO_GLOBAL

from sympy.simplify.fu import L



def lineinput(comando):
    #convirtiendo a string linea ingresada por el usuario
    line=str(comando)
    #Partiendo comando en una lista 
    lines=line.split()

    return lines

class Switcher(object):
    #Matrices creadas o guardadas
    mtrxlist=np.array([])
    mtxans=None
    
    #Agrega una variable a la lista de variables
    @classmethod
    def addmtx(cls,mtx):
        nombre=input("Nombre de la matriz: ")
        #diccionario
        dato = {'id':nombre,'matriz':mtx}
        cls.mtrxlist=np.append(cls.mtrxlist,dato)
        print(Fore.GREEN+"Matriz almacenada")
        print(Fore.WHITE)
    
    #Agrega una variable ans (resultadio de una operacion)
    @classmethod
    def addans(cls,mtx):
        busca=False
        dato=None
        for x in cls.mtrxlist:
            if x['id']=='ans':
                busca=True
                dato=x
        if busca==True:
            x['matriz']=mtx
            print(Fore.GREEN)
            print(x['matriz'])
            print(Fore.WHITE)
        else:
            dato = {'id':'ans','matriz':mtx}
            cls.mtrxlist=np.append(cls.mtrxlist,dato)
            res=cls.busqueda('ans')
            print(Fore.GREEN)
            print(res['matriz'])
            print(Fore.WHITE)
    
    #Busca un elemento en la lista de variables
    @classmethod
    def busqueda(cls,id):
        for x in cls.mtrxlist:
            if x['id']==id:
                return x

    
    #Muestra el menu principal
    def menu(self):
        salir=False
        res=False
        #Lista de metodos

        self.banner()
        while not salir:   
            respuesta=input('\n-> ')
            salir=respuesta=="s"

            data=lineinput(respuesta)
            mtd=""
            #Obteniendo metodo
            if len(data)==3:
                mtd=data[1]
                if mtd=='+':
                    mtd='suma'
                elif mtd=='-':
                    mtd='resta'
                else:
                    mtd=data[1]

            elif len(data)>0:
                mtd=data[0]
            else:
                mtd=None

            nombre_metodo = 'metodo_' + str(mtd)
            metodo = getattr(self, nombre_metodo, lambda default: "No encontrado")
            # Call the method as we return it
            metodo(data)
    
    #Crea una matriz
    def metodo_1(self,argumento=None):
        """Crear una matriz"""
        f=int(input("Numero de filas: "))
        c=int(input("Numero de Columnas: "))
        Mtx=np.zeros((f,c), dtype=complex)
        for k in range(f):
            for l in range(c):
                print("["+str(k+1)+","+str(l+1)+"]",end="")
                z=complex(sy.parse_expr(input("->")))
                Mtx[k][l]=z

        self.addmtx(Mtx)

    #limpia pantalla
    def metodo_l(self,argumento=None):
        m=Switcher()
        #Para linux
        if os.name == "posix":
            os.system ("clear")
            self.banner()
        elif os.name == "ce" or os.name == "nt" or os.name == "dos":
            #Para Windows
            os.system ("cls")
            self.banner()

    def banner(self):
        #banner
        print('-'*30)
        ascii_banner = pyfiglet.figlet_format("Matriz")
        print(Fore.GREEN + ascii_banner)

        #Lista de Opciones
        menu=OrderedDict(
        [
            ('1',"Crear"),
            ('2',"Editar"),
            ('3',"Ver"),
            ('l',"limpiar"),
            ('h',"ayuda"),
            ('s',"salir")
            ]
        )
        #Muestra el menu
        print(Fore.YELLOW)
        for opcion, funcion in menu.items():
            msj_final='[{}]{} '.format(opcion,funcion)
            print(msj_final,end="")
        print(Fore.WHITE)
        
    def editar():
        """Editar Matriz"""
        print("editando")
        
    def metodo_3(self,mtx):
        """Matrices guardadas"""
        print("Matrices guardadas")
        for obj in self.mtrxlist:
            name=Fore.YELLOW+'Id: {}'.format(obj['id'])+Fore.BLUE
            m='\n{}'.format(obj['matriz'])+Fore.WHITE+'\n'
            print(name+m)
    #ayuda
    def metodo_h(self,mtx=None):
        suma="Suma de matrices\n sintaxis: matriz1 + Matriz2 "
        soluciona="\nSolucion de matrices \n sintaxis: matriz1 solve Matriz2 "
        print(suma+soluciona)

    def metodo_suma(self,mtx):
        if len(self.mtrxlist)==0:
            print("No hay ninguna matriz guardada")
        else:
            msj="Suma de matriz"
            print('-'*len(msj))
            print(msj)
            #Obteniendo el nombre de las matrices
            a=mtx[0]
            b=mtx[2]
            x1=None
            x2=None
            bandera1=False
            bandera2=False

            #Buscando en la lista de matrices guardadas 
            for x in self.mtrxlist:
                if x['id']==a:
                    x1=x['matriz']
                    bandera1=True
                if x['id']==b:
                    x2=x['matriz']
                    bandera2=True
           
            if bandera1 and bandera2 == True:
                res=x1+x2
                self.addans(res)
            elif bandera1==False:
                print(Fore.RED+' Matriz ('+a+') no encontrada'+Fore.WHITE)
            elif bandera2==False:
                print(Fore.RED+' Matriz ('+b+') no encontrada'+Fore.WHITE)
    
    def metodo_solve(self,mtx):
        #Obteniendo el nombre de las matrices
        a=mtx[0]
        b=mtx[2]
        x1=None
        x2=None
        bandera1=False
        bandera2=False
        
        for x in self.mtrxlist:
            if x['id']==a:
                x1=x['matriz']
                bandera1=True
            if x['id']==b:
                x2=x['matriz']
                bandera2=True
           
        if bandera1 and bandera2 == True:
            if np.linalg.det(x1) == 0:
                x = None
                print("No se puede resolver")
            else:
                x=np.linalg.solve(x1,x2)
            self.addans(x)
        elif bandera1==False:
            print(Fore.RED+' Matriz ('+a+') no encontrada'+Fore.WHITE)
        elif bandera2==False:
            print(Fore.RED+' Matriz ('+b+') no encontrada'+Fore.WHITE)

    def default(self,argumento=None):
        print("Ingrese una opcion valida")
        


if __name__=='__main__':
    obj=Switcher()
    obj.menu()
