from math import sqrt
import numpy as np
#NOTA: PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
#LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO

#En este espacio podrás programar las funciones que deseas usar en la función solución (NO ES OBLIGATORIO CREAR OTRAS FUNCIONES)
"""Inicio espacio para programar funciones propias"""



#PUEDES PROGRAMAR CUANTAS FUNCIONES DESEES 


"""Fin espacio para programar funciones propias"""

def solucion(a):
    """
    En esta función deberás programar tu solución.
    Explicación del parámetro que recibe:
    - a: Es un vector unidimensionalde numpy, (No te preocupes si NO conoces numpy,
        el manejo que debes darle es IGUAL al de una lista de Python)
        El largo de la lista lo puedes calcular así: L = len(a)
        Para indexar el elemento en la posición i se hace así (Igual como una lista):
            a[i] 
    
            

    Explicación de lo que debe retornar:
    -matriz: Puede ser de dos tipos (COMO TE SIENTAS MÁS CÓMODO)
        Una matriz de numpy O una lista de listas (El calificador está en las condiciones
        para recibit cualquiera de los dos tipos), en esta matriz debes guardar los
        elementos que hay en el vector a como se especifica en el enunciado
    """

    print(type(a))
    if type(a) == type(np.zeros((1))):
        a = a.tolist()
    print(type(a))
    
    #creo la matriz
    '''modo: 𝐿 = 𝑛(𝑛+1)/2'''
    #n1 = int(sqrt(len(a)*2)) #hack
    n = 1
    l= len(a)

    while  l>n*(n+1)/2 :
        n+=1

    #si los datos no son correctos para una matriz cuadrada
    if(n*(n+1)/2 > l):
         print("La entrada de datos es incorrecta. No puedo crear una matriz  triangular inferior en una matriz cuadrada con el numero de datos que ingresaste!")
         exit()
        
    print("valor n ",n)

    matriz = np.zeros((n, n))
    
    for index, data in np.ndenumerate(matriz):
        i = index[0]
        j = index[1]
        if i>=j:
            matriz[i,j] = a.pop(0)
    return matriz
    
"""
Estas líneas de código que siguen, permiten probar si su ejercicio es correcto
"""
#NO MODIFICAR
#l = [8, 60, 72, 35, 26, 75, 15, 12, 33, 54]
l =  np.array([8, 60, 72, 35, 26, 75, 15, 12, 33, 54])
matriz_correcta = np.array([[ 8.,  0.,  0.,  0.], [60., 72.,  0.,  0.], [35., 26., 75.,  0.], [15., 12., 33., 54.]])
matriz_estudiante = np.array(solucion(l))
print("LISTA ENTREGADA:\n", l,"\n")
print("===SALIDA ESPERADA===\nMatriz:\n", matriz_correcta,"\n")
print("===TU SALIDA===\nMatriz:\n", matriz_estudiante,"\n")

for i in range(matriz_correcta.shape[0]):
    for j in range(matriz_correcta.shape[1]):
        if matriz_correcta[i,j] != matriz_estudiante[i,j]:
            print("Las salidas no coinciden, ¡Estás olvidando algo en tu código!")
            exit()
print("Todo se ve correcto, ¡Procede a calificar tu código!")