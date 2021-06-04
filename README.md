## Ingresando matriz
\left[\begin{matrix}23 x^{2}\end{matrix}\right]
__ __ _ _

    | \/ | __ _| |_ _ __(_)____ 
    | |\/| |/ _` | __| '__| |_ /
    | | | | (_| | |_| | | |/ /
    |_| |_|\__,_|\__|_| |_/___|
    
      
      
      
    
    Slot:[m1] [m2] [m3] [m4] [m5] [m6] [m7] [m8] [m9] [ans]
    
    [1] Opciones
    
    [2] Limpiar
    
    [s] Salir

------------------------------

->

Escribe el numero de la opción correspondiente

  

    -> 1

    ___ _
    / _ \ _ __ ___(_) ___ _ __ ___ ___
    | | | | '_ \ / __| |/ _ \| '_ \ / _ \/ __|
    | |_| | |_) | (__| | (_) | | | | __/\__ \
    \___/| .__/ \___|_|\___/|_| |_|\___||___/
    |_|
    
      
      
    
    Slot:[m1] [m2] [m3] [m4] [m5] [m6] [m7] [m8] [m9] [ans]
    
      
    
    [1] Crear
    
    [2] Editar
    
    [3] Eliminar
    
    [4] Ayuda
    
    [0] Volver

  

Elije la opcion 1

    ->1

  

El programa pedirá los datos correspondientes

    Numero de filas: 2
    
    Numero de columnas: 2
    
        [1,1]-> 1
        
        [1,2]-> 2
        
        [2,1]-> 3
        
        [2,2]-> 4

Ahora deberás colocar el numero del slot donde deseas guardarlo

existen 9 slot disponibles

  

Slot a guardar (1-9)->

Una vez hecho esto nos mostrara un mensaje de confirmación

  

Matriz almacenada-> slot m1

  

## Slot de memoria

  

**Definidos como:**

  

-  `m1` Es un slot 1

-  `m2` Es un slot 2

-  `m3` Es un slot 3

  

-  `ans` : *Este almacena la respuesta de ultima operación realizada*

  

## **Operaciones **

  

Suma de matrices

`m1 + m2`

  

Resta de matrices

`m1 - m2`

  

Multiplicacion

`m1 * m2`

  

Determinante

`det m1`

  

Inversa

`inv m1`

  

Transpuesta

`trn m1`

  

## Resuelve sistemas de ecuaciones

Donde `m1` es la matriz aumentada

`solve m1`
***Ejemplo***
	Sistema de ecuaciones
	$\left.  
	\begin{array}{rcl}  
	(2 + \frac{1}{s})J_1 & (\frac{1}{s})J_2 & = & v  
	\\ (\frac{1}{s})J_1 & (4 + \frac{1}{s})J_2 &= & 0  
	\end{array}  
	\right\}$

Matriz aumentada
slot[m1]->$\left[\begin{matrix}2 + \frac{1}{s}  & \frac{1}{s} & v\\\frac{1}{s} & 4 + \frac{1}{s} & 0\end{matrix}\right]$

Matriz columna respuesta
$\left
[\begin{matrix}\frac{v \left(4 s + 1\right)}{2 \left(4 s + 3\right)}
\\ - \frac{v}{8 s + 6}\end{matrix}
\right]$

Donde
$\left.  
	\begin{array}{rcl}  
	J_1& = & \frac{v \left(4 s + 1\right)}{2 \left(4 s + 3\right)}
	\\ J_2 &= & - \frac{v}{8 s + 6} 
	\end{array}  
	\right\}$

## Expande

Expande los valores contenidos dentro del slot

(util si se tiene expresiones algebraicas)

`expande m1` 

Expande los valores contenidos dentro del slot `ans`
`expande`  

**Ejemplo** 
$\left[\begin{matrix}\frac{v \left(4 s + 1\right)}{2 \left(4 s + 3\right)}\\- \frac{v}{8 s + 6}\end{matrix}\right]$

 **Expandido**
$\left[\begin{matrix}\frac{4 s v}{8 s + 6} + \frac{v}{8 s + 6}\\- \frac{v}{8 s + 6}\end{matrix}\right]$

## Simplifica

Simplifica los valores contenidos dentro del slot

(util si se tiene expresiones algebraicas)
> -> m1
> $\left[\begin{matrix}\frac{4 s v}{8 s + 6} + \frac{v}{8 s + 6}\\- \frac{v}{8 s + 6}\end{matrix}\right]$
> 
`simplifica m1`
> $\left[\begin{matrix}\frac{v \left(4 s + 1\right)}{2 \left(4 s +
> 3\right)}\\- \frac{v}{8 s + 6}\end{matrix}\right]$

  

## Codigo Latex

Imprime el codigo latex de la expresion guardada en un slot

> -> m1

$\left[\begin{matrix}\frac{v \left(4 s + 1\right)}{2 \left(4 s + 3\right)}\\- \frac{v}{8 s + 6}\end{matrix}\right]$

`latex m1`

> -> latex m1 
> **\left[\begin{matrix}\frac{v \left(4 s + 1\right)}{2 \left(4 s + 3\right)}\\- \frac{v}{8 s + 6}\end{matrix}\right]**

  

## Codigo

Imprime la expresion (legible por el programa) guardada en un slot

     -> m1 

$\frac{v \left(4 s + 1\right)}{2 \left(4 s + 3\right)}$

`-> code m1`

     v*(4*s + 1)/(2*(4*s + 3))
  
## Fracciones parciales

Exapande en fracciones parciales el contenido dentro de una matriz (slot ans)

`fracciones`

***Expresión***
$\bigl
|\begin{matrix}\frac{x^{2} + 2 x + 3}{x^{3} + 4 x^{2} + 5 x + 2}\end{matrix}
\bigr|$

***Resultado***
$\bigl
[\begin{matrix}\frac{3}{x + 2} - \frac{2}{x + 1} + \frac{2}{\left(x + 1\right)^{2}}\end{matrix}
\bigr|$	
  
  

## Guarda en

Guarda la ultima operacion realizada dentro de un slot

`g`

  

## Aun en desarrollo

  

[2]Editar: Edita los valores dentro de la matriz

[3]Ayuda: Mensaje de ayuda con los comandos
