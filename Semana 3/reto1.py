"""
El siguiente código ha perdido algunas de sus líneas.  Su trabajo es completar las líneas de código que faltan, 
las cuales están marcadas claramente con textos que describen lo que la línea debe hacer. 
Todo el programa realiza las siguientes acciones:

Se genera un entero entre 15 y 30; luego, luego se construye un objeto de la clase vector 
(esta clase ya existe) tal como la definida en el curso. El tamaño del vector es el número generado 
inicialmente. Luego, se llena el vector con números enteros entre 1 y 9999 generados aleatoriamente.

Posteriormente se crea una variable suma, inicializada en cero, donde vamos a guardar la suma de 
los datos del vector que sean primos o que comiencen con dígito impar.

Lea atentamente los comentarios que hay en el código a su disposición, para obtener el resultado 
de su evaluación complete las funciones presentadas comenzando por la función solucion(), 
en los comentarios se les indicará en qué momento completar las otras dos funciones. 
La función solucion() debe retornar respectivamente el vector construido inicialmente y la variable donde sumó.

En otras palabras, la última instrucción del método solución, sería:

return nombreDelVectorCreado, nombreDelaVariableDondeSumó

Si el vector creado se llamó vec5 y la suma se llamó s, sería:

return vec5, s

Ejemplo:

vector original = 30, 23, 19, 18, 7, 21, 31, 12, 41, 9

Los números que se suman son 30, 23, 19, 18, 7, 31, 12, 41, 9; por lo tanto la suma es 190.

los primos son : 7,19,23,31,41
lo que tiene primera cifra inpar son 30,18,12,9

"""



#from vector import vector
import random
import math


#INICIE COMPLETANDO LA FUNCIÓN SOLUCIÓN
def solucion():
    """Completa la siguiente línea para generar un número entero aleatorio 
    entre 15 y 30.
    Sugerencia, usa random.randint"""
    #a = #Completar
    a = random.randint(15,30)
    
    """Creación del objeto vector con tamaño a"""
    #v = vector(a)
    v = [None] * a
    
    """Llenar el vector con números enteros aleatorios entre 1 y 9999.
    Recuerde que en el curso se definió que se debe llenar desde 
    la posición 1 en adelante, pues la posición cero guarda el número
    de casillas ocupadas en el vector con números diferentes de cero"""
    for i in range(1, a + 1):
        
        """Completa el llenado de cada casilla, el número debe ser entero y 
        aleatorio entre 1 y 9999.
        Sugerencia, usa random.randint"""
        #v.V[i] =   random.randint(1,999)#Completar
        v[i-1] =   random.randint(1,999)#Completar
      
        
        """Como el número es aleatorio entre 1 y 9999, habrá UNA (1) nueva casilla
        ocupada, por lo tanto, se debe ir alterando en UNO (1) la posición 0 del vector
        cada vez que se llene una casilla"""
        #v.V[0] += 1
        #v[i] += 1

    #Vamos a completar la función es_primo, (línea 54)
    
    #SIGAMOS COMPLETANDO LA FUNCIÓN SOLUCIÓN
    """Creamos una variable s, donde guardaremos la suma de los números 
    que son primos o que comienzan por dígito impar"""
    s = 0
    
    """Recorramos todas las casilla del vector (Desde la posición 1)
    Complete los límites de la función range:"""
    #for i in range(1,v.len()): #Completar

    #dnto
    #v = [30, 23, 19, 18, 7, 21, 31, 12, 41, 9]

    for i in range(0,len(v)): #Completar
        
        """Si el número guardado en la posición i es primo o comienza por dígito impar
        SÚMELO a la variable s
        Complete el siguiente condicional, para que sume solo los números primos
        o números que empiecen por dígito impar:"""
        if es_primo(v[i]) or comienza_digito_impar(v[i]): #Completar
            #s += v.V[i]
            s += v[i]
            
    #El ejercicio ha terminado, PRUEBA TU SOLUCIÓN (Click en la nave espacial)
    # Presiona en evaluar para entregar el ejercicio :D
    return v, s

def es_primo(n):
    """
    Esta función retorna True si el número n es primo
    Retorna False si el número n NO es primo
    
    -Un número primo es un número que SOLO es divisible por él mismo y el 1.
    Ejemplos: 2, 3, 5, 7, 11, 13, y el 17 son números primos.
    
    -Un número k es divisible por d si k módulo d es cero: k % d == 0
    Ejemplos:8 es divisible por 4, 9 es divisible por 3, 27 es divisible por 3.
    
    Comprobemos si el número n es un número primo, para ello se hará lo siguiente:
        Probar si n es divisible por un número entre 2 y n-1.
        En caso de que NO haya ningún número tal que n sea divisible por él, retornamos True (Sí es primo), pero si hay 
        al menos UN número en ese intervalo que divida a n, retornamos False (No es primo)
    Complete los límites del ciclo (los límites en la función range)"""
    for d in range(2,n): #Completar
        
        """Complete cuál es la condición que se debe cumplir para que un número NO sea primo
        Ayuda: si n es divisible por d, entonces n NO es primo"""
        if n % d == 0: #Completar
        
            """Si entra a este condicional, es porque hay un número que divide a n, por tanto NO es primo"""
            return False
            
    """Si logra salir de este ciclo, es porque no hayó ningún número que divida a n, por tanto SÍ es primo"""
    #Vamos a completar la función comienza_digito_impar, (línea 84)
    return True

def comienza_digito_impar(n):
    """Esta función retorna True si n comienza por un dígito impar, ejemplo de números que
    comienzan por dígito impar: 1234, 76555, 92228
    Retorna False si n NO comienza por dígito impar
    
    Complete la siguiente línea, que sirve para guardar el primer dígito de n en una variable llamada d"""
    d = str(n)[0] #Completar
    
    """d guarda un valor de tipo texto, completa la siguiente línea para cambiar el tipo de la variable d a entero"""
    d = int(d) #Completar
    
    """Un número d es impar si d % 2 == 1
    Complete cuál es la condición que se debe cumplir para que un número SÍ sea impar"""
    if d % 2 != 0:
    
        """Si entra a este condicional, es porque n empieza por un dígito impar"""
        return True
        
    """Si NO entra al condicional anterior, es porque n NO empieza por un dígito impar"""
    #Vamos a seguir completando la función solución, (línea 34)
    return False
   
   
   
    
"""Esta función permite imprimir vectores en la consola"""

def imprimeVector(vector, mensaje="vector sin nombre: \t"):
    print("\n", mensaje, end="        ")
    #for i in range(1, vector.V[0] + 1):
    for i in range(0, len(vector)):
        #print(vector.V[i], end=", ")
        print(vector[i], end=", ")
        if i % 30 == 0:
            print("\n                      ", end="")
    print()
    
"""Las siguientes líneas le permitirán probar su solución al presionar el botón de ejecutar"""
a, suma = solucion()
imprimeVector(a, 'Original')
print("Suma: ", suma)