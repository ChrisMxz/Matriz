from collections import OrderedDict
from operator import le
import os
from numpy.lib.function_base import append
import pyfiglet
from colorama import Fore
from sympy import *
import sympy as sy
import numpy as np
from sympy.simplify.fu import L 

class Mtrx():
    #Matrices creadas o guardadas
    #Constructor sin parametros
    def __init__(self):
        self.mtrxlist={
            'm1':[False,None],
            'm2':[False,None],
            'm3':[False,None],
            'm4':[False,None],
            'm5':[False,None],
            'm6':[False,None],
            'm7':[False,None],
            'm8':[False,None],
            'm9':[False,None],
            'ans':[False,None]
        }
        self.letras=None
    
    #Sobre carga de operadores
    def suma(self,comandos=None):
        l=self.mtrxlist['1']
        l2=self.mtrxlist['2']
        try:
            r=l[1]+l2[2]
            print(r)
        except Exception:
            print("No se puede realizar la suma (verifica las dimenciones)")
        

    
    #Metodos
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
            ('3',"Eliminar"),
            ('4',"Ver"),
            ('5',"Limpiar_Pantalla"),
            ('6',"Ayuda"),
            ('0',"Salir")
            ]
        )
        #Muestra el menu
        print(Fore.YELLOW)
        for opcion, funcion in menu.items():
            msj_final='[{}]{} '.format(opcion,funcion)
            print(msj_final,end="")
        print(Fore.WHITE)

    #limpia pantalla
    def met_5(self,argumento=None):
        #Para linux
        if os.name == "posix":
            os.system ("clear")
            self.banner()
        elif os.name == "ce" or os.name == "nt" or os.name == "dos":
            #Para Windows
            os.system ("cls")
            self.banner()

    def busqueda(self,id=None):
        dato=False
        for x in self.mtrxlist:
            if x==id:
                dato=True
        return dato
    
    def crea_dic(self):
        palabra = 'abcdefghklmnopqrstuvwxyz'
        d = dict()
        for c in palabra:
            if c not in d:
                d[c] = 1
            else:
                d[c] = d[c] + 1
        self.letras=d
    
    #Da formato a la matriz (imprime)
    def formato_mtx(self,mtx):
        dato=str(mtx)
        dato=dato.replace("[","|")
        dato=dato.replace("]","|")
        return dato

    #transforma string de entrada en segemntos de definidos por un espacio
    def lineinput(self,comando=None):
        #convirtiendo a string linea ingresada por el usuario
        line=str(comando)
        #Partiendo comando en una lista 
        lines=line.split()
        return lines
    
    #Entrada de un numero para la matriz
    def input_complex(self):
        bandera=False
        while not bandera:
            en=str(input())
            if len(en)>0:
                try:
                    z=complex(sy.parse_expr(en))
                    bandera=True
                except Exception:
                    print("Numero no valido-> ",end='')
        return z
    
    #Restige la entrada a solo numeros enteros para seleccion
    def input_num(self):
        bandera=False
        while not bandera:
            num=input()
            if num.isdigit()==True:
                num=int(num)
                bandera=True
        return num
    
    #Agrega una matriz al diccionario de variables
    def addmtx(self,mtx):
        listo=False
        print("Slot a guardar (1-9)-> ",end="")

        while not listo:
            slot=self.input_num()
            if slot>0 and slot<10:
                listo=True
        
        slot=str("m"+str(slot))
        #Agregando al slot
        l=self.mtrxlist[slot]
        l[0]=True
        l[1]=mtx
        print(Fore.GREEN+"Matriz almacenada-> slot "+slot)
        print(Fore.WHITE)
    
    #Guarda la matriz ans (resultado de una operacion)
    #en un slot de memoria definido por el usuario
    def asignar(self):
        l=self.mtrxlist['ans']
        m=l[1]
        self.addmtx(m)
    
    def respuesta(self,res=None):
        l=self.mtrxlist['ans']
        l[0]=True
        l[1]=res
    #Muestra todos las matrices guardadas
    def met_4(self,arg=None):
        print("Matrices guardadas")
        print(Fore.GREEN+'[Usado] '+Fore.RED+'[Vacio] '+Fore.WHITE)
        print("Slot:",end="")
        bandera=False
        for obj in self.mtrxlist:
            l=self.mtrxlist[obj]#Obtiene la lista
            status=l[0]
            if status==False:
                print(Fore.RED,end='')
            else:
                print(Fore.GREEN,end='')
            if obj=='ans':
                m='[10'+obj+'] '
            else:
                m='['+obj+'] '
            print(m,end="")
            
        while not bandera:
            listo=False
            print(Fore.WHITE)
            print("Ver slot-> ",end="")
            
            while not listo:
                slot=self.input_num()
                if slot>0 and slot<11:
                    listo=True
            if slot==10:
                slot='ans'
                l=self.mtrxlist[slot]
            else:
                l=self.mtrxlist["m"+str(slot)]

            if l[0]==False:
                msj=Fore.RED+"Slot ["+str(slot)+"]\n"+"Vacio"
            else:
                msj=Fore.GREEN+"Slot ["+str(slot)+"]\n\n"+self.formato_mtx(l[1])
            print('-'*len(msj))
            print(msj+Fore.WHITE)
            print(Fore.YELLOW+"\nsalir[s/n]",end=''+Fore.WHITE)
            salir=str(input("-> "))
            if salir =='s':
                bandera=True

    #Crea una matriz
    def met_1(self,argumento=None):
        print("Numero de filas: ",end='')
        f=self.input_num()
        print("Numero de columnas: ",end='')
        c=self.input_num()
        Mtx=np.zeros((f,c), dtype=complex)
        for k in range(f):
            for l in range(c):
                print("["+str(k+1)+","+str(l+1)+"]",end="")
                z=complex(sy.parse_expr(input("-> ")))
                Mtx[k][l]=z
        self.addmtx(Mtx)
    
    #Muestra el menu principal
    def metodo(self,opc):
        dato=None
        nombre_metodo ="met_"+str(opc)
        metodo = getattr(self, nombre_metodo, lambda default: "No encontrado")
        metodo(dato)


    def menu(self):
        salir=False
        res=False
        self.met_5()
        #Bucle para mantenerse en el programa
        while not salir:   
            x=input("-> ")
            entrada=self.lineinput(x)
            #Vericando los 3 opciones
            if len(entrada)==3:
                #Es una instruccion estilo: m1 + m3
                if self.busqueda(entrada[0])==True and self.busqueda(entrada[2])==True:
                    #Obteniendo las variables a operar
                    l=self.mtrxlist[str(entrada[0])]
                    l2=self.mtrxlist[str(entrada[2])]
                    ma=l[1]
                    mb=l2[1]
                    #verifocando operador
                    try:
                        if entrada[1]=='+':
                            res=ma+mb
                            self.respuesta(res)
                            print(Fore.GREEN+self.formato_mtx(res)+Fore.WHITE)
                        elif entrada[1]=='-':
                            res=ma-mb
                            self.respuesta(res)
                            print(Fore.GREEN+self.formato_mtx(res)+Fore.WHITE)
                        elif entrada[1]=='*':
                            res = np.dot(ma,mb)
                            self.respuesta(res)
                            print(Fore.GREEN+self.formato_mtx(res)+Fore.WHITE)
                        elif entrada[1]=='x':
                            res = np.cross(ma,mb)
                            self.respuesta(res)
                            print(Fore.GREEN+self.formato_mtx(res)+Fore.WHITE)
                        else:
                            print(Fore.RED+"Operacion no especificada"+Fore.WHITE)
                    except Exception:
                                print(Fore.RED+"Verifica tus matrices"+Fore.WHITE)
            
            elif len(entrada)==2:
                #Es una instruccion estilo: trasnpuesta m3
                 print("tiene 2 elementos")
            elif len(entrada)==1:
                opc=entrada[0]   
                if opc.isdigit()==True:
                    opc=int(opc)
                    if opc<7 and opc>0:
                        self.metodo(opc)
                    elif opc==0:
                        salir=True
                        print("Saliendo")
            else:
                print("Escribe bien la instruccion")
 


if __name__=='__main__':
    mt1=Mtrx()
    mt1.menu()