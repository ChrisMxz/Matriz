from collections import OrderedDict
from operator import le
import os
import pyfiglet
from colorama import Fore
from sympy import *
import sympy as sy
import numpy as np
from sympy.simplify.fu import L 
from sympy.abc import X, s,v,z,f
import copy

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
            'm10':[False,None],
            'ans':[False,None]
        }
        self.letras=None
    #guarda las variables en un txt para la proxima vez que se habra el programa
    def guardado_memoria(self,arg=None):
        txt="slots guardados\n"
        for i in self.mtrxlist:
            l=self.mtrxlist[i]
            if l[0]==True:
                matriz=l[1]
                np.savetxt(str(i)+".txt",matriz)
                txt=txt+str(i)+'\n'
        fichero = open('info.txt','w')
        fichero.write(txt)
        fichero.close
    
    #Metodos
    def banner(self,text):
        #banner
        ascii_banner = pyfiglet.figlet_format(text)
        print(Fore.GREEN + ascii_banner)
        print(Fore.WHITE)
        self.line_var_status()
        if text=="Opciones":
            #Lista de Opciones
            menu=OrderedDict(
            [
                ('1',"Crear"),
                ('2',"Editar"),
                ('3',"Eliminar"),
                ('4',"Ayuda"),
                ('0',"Volver")
                ]
            )
            #Muestra el menu
            print(Fore.YELLOW)
            for opcion, funcion in menu.items():
                msj_final='[{}] {} '.format(opcion,funcion)
                print(msj_final)
            print(Fore.WHITE)
        elif text=="Matriz":
            print(Fore.YELLOW+"[1] Opciones\n[2] Limpiar\n[s] Salir"+Fore.WHITE)
            print('-'*30)
        elif text=="Crear":
            print(Fore.YELLOW+"Ingresa los datos correspondientes de la matriz"+Fore.WHITE)
            print('-'*30)
        


    #limpia pantalla
    def limpiar(self,argumento=None):
        #Para linux
        if os.name == "posix":
            os.system ("clear")
            self.banner(argumento)
        elif os.name == "ce" or os.name == "nt" or os.name == "dos":
            #Para Windows
            os.system ("cls")
            self.banner(argumento)
            
            
    def busqueda(self,id=None):
        dato=False
        for x in self.mtrxlist:
            if x==id:
                dato=True
        return dato
    def imprimir(self,mtx):
        if mtx[0]==False:
            print(Fore.RED+"Vacio")
        else:
            print(Fore.GREEN)
            print(pretty(mtx[1]))
            #pprint(mtx[1], use_unicode=False)

        print(Fore.WHITE)
        print('-'*30)
        
    
    def crea_dic(self):
        palabra = 'abcdefghklmnopqrstuvwxyz'
        d = dict()
        for c in palabra:
            if c not in d:
                d[c] = 1
            else:
                d[c] = d[c] + 1
        self.letras=d
   
    #transforma string de entrada en segemntos de definidos por un espacio
    def lineinput(self,comando=None):
        #convirtiendo a string linea ingresada por el usuario
        line=str(comando)
        line.lower()
        #Partiendo comando en una lista 
        lines=line.split()
        return lines
    
    #Entrada de dato para la matriz
    def input_dato(self):
        bandera=False
        while not bandera:
            en=str(input())
            if len(en)>0:
                try:
                    z=sy.parse_expr(en)
                    bandera=True
                except Exception:
                    print(Fore.YELLOW+"Expresion no valida"+Fore.WHITE)
                    print("-> ",end='')
        return z
    def get_posicion(self,mtx=None):
        salir =False
        dimension=mtx.shape
        f=dimension[0]
        c=dimension[1]
        print(Fore.BLUE+pretty(mtx)+Fore.WHITE)
        print("Dimension ["+str(f)+","+str(c)+"]")
        print("Posicion:")
        while not salir:
            print("Fila-> ",end='')
            k=self.input_num()
            k=k-1
            if k>=0 and k<f:
                salir=true
            else:
                print("Vuelva a intentarlo")
        salir=False
        while not salir:
            print("Columna-> ",end='')
            l=self.input_num()
            l=l-1
            if l>=0 and l<c:
                salir=true
            else:
                print("Vuelva a intentarlo")
        posicion=(k,l)
        return posicion

    #Obtiene un dato dentro de una matriz
    def get_dato(self, mtx=None):
        pos=self.get_posicion(mtx)
        k=pos[0]
        l=pos[1]
        print("\nDato ["+str(k+1)+","+str(l+1)+"]")
        dato=mtx[k,l]
        print(Fore.GREEN+pretty(dato)+Fore.WHITE)
        self.respuesta(dato) #guardamos en ans
    

    #Restige la entrada a solo numeros enteros para seleccion
    def input_num(self):
        bandera=False
        while not bandera:
            num=input()
            if num.isdigit()==True:
                num=int(num)
                bandera=True
            else:
                print(Fore.YELLOW+"Vuelve a intentarlo-> "+Fore.WHITE,end='')
        return num
    
    #Agrega una matriz al diccionario de variables
    def addmtx(self,mtx):
        listo=False
        n=len(self.mtrxlist)
        print("Slot (1-"+str(n-1)+")-> ",end="")

        while not listo:
            slot=self.input_num()
            if slot>0 and slot<n:
                listo=True
        
        slot=str("m"+str(slot))
        #Agregando al slot
        l=self.mtrxlist[slot]
        l[0]=True
        l[1]=mtx
        print(Fore.GREEN+pretty(mtx))
        print("Guardado -> slot "+slot)
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
    def line_var_status(self,arg=None):
        #print("Matrices guardadas")
        #print(Fore.GREEN+'[Usado] '+Fore.RED+'[Vacio] '+Fore.WHITE)
        print("Slot:",end="")
        bandera=False
        for obj in self.mtrxlist:
            l=self.mtrxlist[obj]#Obtiene la lista
            status=l[0]
            if status==False:
                if obj=="ans":
                    print(Fore.BLUE,end='')
                else:
                    print(Fore.RED,end='')
            else:
                if obj=="ans":
                    print(Fore.BLUE,end='')
                else:
                    print(Fore.GREEN,end='')
            m='['+obj+'] '
            print(m,end="")
        print(Fore.WHITE)
            
    #Crea una matriz
    def met_1(self,argumento=None):
        self.limpiar("Crear")
        print("Numero de filas: ",end='')
        f=self.input_num()
        print("Numero de columnas: ",end='')
        c=self.input_num()
        Mtx=sy.Matrix.zeros(f,c)
        for k in range(f):
            for l in range(c):
                print("["+str(k+1)+","+str(l+1)+"]-> ",end="")
                z=self.input_dato()
                Mtx[k,l]=z       
        self.addmtx(Mtx)

    def met_2(self,met=None):
        self.limpiar("Editar")
        print("??Cual slot desea editar?")
        listo=False
        n=len(self.mtrxlist)
        print("Slot (1-"+str(n-1)+")-> ",end="")
        while not listo:
            slot=self.input_num()
            if slot>0 and slot<n:
                listo=True
        
        slot=str("m"+str(slot))
        l=self.mtrxlist[slot]
        mtx=l[1]
        pos=self.get_posicion(mtx)
        print(Fore.BLUE+"Dato a remplazar: ")
        print(pretty(mtx[pos[0],pos[1]]))
        print(Fore.YELLOW+"Nuevo dato-> ",end='')
        x=self.input_dato()
        mtx[pos[0],pos[1]]=x
        print(Fore.GREEN+"Valor editado")
        print(pretty(mtx)+Fore.WHITE)

    def met_3(self,arg=None):
        self.limpiar("Eliminar")
        salir=False
        print("??Cual slot deseas eliminar?")
        while not salir:
            print("-> ",end='')
            x=self.input_num()
            if x<10 and x>0:
                l=self.mtrxlist["m"+str(x)]
                l[0]=False
                l[1]=None
                salir=True
        print(Fore.RED+"Eliminado -> [m"+str(x)+"]"+Fore.WHITE)
        

    #Ejecuta el metodo seleccionado
    def metodo(self,opc):
        dato=None
        nombre_metodo ="met_"+str(opc)
        metodo = getattr(self, nombre_metodo, lambda default: "No encontrado")
        metodo(dato)
    
    def opciones(self):
        bandera = False
        while not bandera:
            self.limpiar("Opciones")
            print("->",end='')
            opc=self.input_num()
            if opc<8 and opc>0:
                self.metodo(opc)
                input("Presione una tecla para continuar...")
            elif opc==0:
                bandera=True
                self.limpiar("Matriz")
            else:
                print(Fore.YELLOW+"Elige una opcion valida"+Fore.WHITE)
                input("Presione una tecla para continuar...")
            
            
   
    def menu(self):
        salir=False
        res=False
        r=self.mtrxlist["ans"]
        self.limpiar("Matriz")
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
                    #verificando operador
                    try:
                        if entrada[1]=='+':
                            res=ma+mb
                            res= sy.simplify(res)
                            self.respuesta(res)
                            self.imprimir(r)
                        elif entrada[1]=='-':
                            res=ma-mb
                            res= sy.simplify(res)
                            self.respuesta(res)
                            self.imprimir(r)
                        elif entrada[1]=='*':
                            res = ma*mb
                            res= sy.simplify(res)
                            self.respuesta(res)
                            self.imprimir(r)
                        elif entrada[1]=='x':
                            print("desarrollo")
                            #res = ma**mb
                            #self.respuesta(res)
                            #self.imprimir(r)
                        else:
                            print(Fore.RED+"Operacion no especificada"+Fore.WHITE)
                    except Exception:
                            print(Fore.RED+"Verifica tus matrices"+Fore.WHITE)
                elif self.busqueda(entrada[2])==True:
                    # <valor> * <matriz>
                    #Obteniendo las variables a operar
                    l=self.mtrxlist[str(entrada[2])]
                    ma=l[1]
                    #verificando operador
                    try:
                        if entrada[1]=='*':
                            res = sy.parse_expr(entrada[0])*ma
                            res= sy.simplify(res)
                            self.respuesta(res)
                            self.imprimir(r)
                        else:
                            print(Fore.RED+"Operacion no permitida"+Fore.WHITE)
                    except Exception:
                                print(Fore.RED+"Verifica tus matriz"+Fore.WHITE)
                elif self.busqueda(entrada[0])==True:
                    # <matriz> * <valor>
                    #Obteniendo las variables a operar
                    l=self.mtrxlist[str(entrada[0])]
                    ma=l[1]
                    #verificando operador
                    try:
                        if entrada[1]=='*':
                            res = sy.parse_expr(entrada[2])*ma
                            res= sy.simplify(res)
                            self.respuesta(res)
                            self.imprimir(r)
                        else:
                            print(Fore.RED+"Operacion no permitida"+Fore.WHITE)
                    except Exception:
                                print(Fore.RED+"Verifica tus matriz"+Fore.WHITE)
            
            elif len(entrada)==2:
                #Es una instruccion estilo: trasnpuesta m3
                 if self.busqueda(entrada[1])==True: # <comando> <matriz>
                    l=self.mtrxlist[str(entrada[1])]
                    ma=l[1]
                    if entrada[0]=="det":
                         try:
                            res= ma.det()
                            res= sy.simplify(res)
                            self.respuesta(res)
                            self.imprimir(r)
                         except Exception:
                            print("No se puede calcular el determinante de esta matriz")
                    elif entrada[0]=="inv":
                        try:
                            res=ma**-1
                            res= sy.simplify(res)
                            self.respuesta(res)
                            self.imprimir(r)
                        except Exception:
                            print("No se puede calcular la inversa de esta matriz")
                    elif entrada[0]=="trn":
                        try:
                            res=ma.T
                            res= sy.simplify(res)
                            self.respuesta(res)
                            self.imprimir(r)
                        except Exception:
                            print("No se puede calcular la transpuesta de esta matriz")
                    elif entrada[0]=="solve":
                        try:
                            A=ma[:,:]
                            b=A.col(-1)
                            A.col_del(-1)
                            res= A.solve(b,method='GJ')
                            res= sy.simplify(res)
                            self.respuesta(res)
                            self.imprimir(r)
                        except Exception:
                            print("No se puede resolver el sistema")

                    elif entrada[0]=="latex":
                        try:
                            print(latex(ma))
                        except Exception:
                            print("Memoria vacia")
                    elif entrada[0]=="code":
                        try:
                            print(ma)
                        except Exception:
                            print("Memoria vacia")
                        #Guarda ans -> en un slot
                    #expande lo guardado en la memoria indicada
                    elif entrada[0]=="expande":
                        try:
                            res=sy.expand(ma)
                            self.respuesta(res)
                            self.imprimir(r)
                        except Exception:
                            print("No se puede ralizar la accion")
                    #simplifica lo guardado en la memoria indicada
                    elif entrada[0]=="simplifica":
                        try:
                            res=sy.simplify(ma)
                            self.respuesta(res)
                            self.imprimir(r)
                        except Exception:
                            print("No se puede ralizar la accion")
                    #Factoriza 
                    elif entrada[0]=="factoriza":
                            try:
                                res=sy.factor(ma)
                                self.respuesta(res)
                                self.imprimir(r)
                            except Exception:
                                print("No se puede ralizar la accion")
                    #Fraccciones parciales a lo almacenado en el slot ans
                    elif entrada[0]=="fracciones":
                            try:
                                res=sy.apart(ma)
                                self.respuesta(res)
                                self.imprimir(r)
                            except Exception:
                                print("No se puede ralizar la accion")

                    elif entrada[0]=="get":
                        try:
                            dato=self.get_dato(ma)
                        except Exception:
                            print(Fore.YELLOW+entrada[1]+"\nNo es una matriz o esta vacia"+Fore.WHITE)

            elif len(entrada)==1:
                if self.busqueda(entrada[0])==True:#verifica si es una variable guardada
                    l=self.mtrxlist[entrada[0]]
                    self.imprimir(l)
                elif entrada[0]=="g":
                        try:
                            l=self.mtrxlist['ans']
                            ans=l[1]
                            self.addmtx(ans)
                        except Exception:
                            print("No se puede ralizar la accion")
                #expande lo almacenado en el slot ans
                elif entrada[0]=="expande":
                        try:
                            l=self.mtrxlist['ans']
                            ans=l[1]
                            res=sy.expand(ans)
                            self.respuesta(res)
                            self.imprimir(r)
                        except Exception:
                            print("No se puede ralizar la accion")
                #Factoriza lo almacenado en el slot ans
                elif entrada[0]=="factoriza":
                        try:
                            l=self.mtrxlist['ans']
                            ans=l[1]
                            res=sy.factor(ans)
                            self.respuesta(res)
                            self.imprimir(r)
                        except Exception:
                            print("No se puede ralizar la accion")
                #Fraccciones parciales a lo almacenado en el slot ans
                elif entrada[0]=="fracciones":
                        try:
                            l=self.mtrxlist['ans']
                            ans=l[1]
                            res=sy.apart(ans)
                            self.respuesta(res)
                            self.imprimir(r)
                        except Exception:
                            print("No se puede ralizar la accion")
                
                elif entrada[0]=="s":
                    salir=True
                    print("Saliendo")
                elif entrada[0]=="1":
                    self.opciones()
                elif entrada[0]=="2":
                    self.limpiar("Matriz")
            else:
                print("!Escribe bien la instruccion??")
 


if __name__=='__main__':
    mt1=Mtrx()
    mt1.menu()
    #mt1.guardado_memoria()
    #mt1.opciones()