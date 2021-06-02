from collections import OrderedDict
from operator import le
import os
import pyfiglet
from colorama import Fore
from sympy import *
import sympy as sy
import numpy as np
from sympy.simplify.fu import L 

def met_2(argumento=None):
        print("Numero de filas: 3")
        print("Numero de columnas: 3")
        mx=sy.Matrix.zeros(3,3)
        print(pretty(mx))
        mx[0,0]=12
        mx[0,1]=15
        print(pretty(mx))
        
met_2()