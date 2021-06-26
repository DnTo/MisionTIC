#NO ELIMINAR LAS SIGUIENTES IMPORTACIONES, sirven para probar tu código en
#consola, y el funcionamiento de la clase cliente
#from pruebas import pruebas_codigo_estudiante
from cliente import cliente
"""NOTAS: 
    -PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
    -LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO
"""


"""Inicio espacio para programar funciones propias"""
#En este espacio podrás programar las funciones que deseas usar en la función
#solución (ES OPCIONAL
def get_edad(cliente):
    return cliente.edad

def get_valor_consignar(cliente):
    return cliente.cantidad_consignar

def get_valor_retirar(cliente):
    return cliente.cantidad_retirar

def get_transaccion(cliente):
    return cliente.transaccion



"""Fin espacio para programar funciones propias"""

def sede_bancaria(cola_general):
    #ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN
    #EL ENUNCIADO.
 #ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN EL ENUNCIADO.
    cola_caja = []
    cola_info = []
    suma_retiros = 0
    suma_consignaciones = 0
    edad_minima_retiro = 99
    edad_minima_info = 99
    edad_minima_consignacion = 99
    
   # for index,cli in enumerate(cola_general):
    for cli in cola_general:
        print(cli.nombre, cli.fila_interes,cli.edad,cli.transaccion)
        if(cli.fila_interes.upper() == "CAJA"):
            #cola_caja.append(cola_general[index].nombre)
            cola_caja.append(cli.nombre)
            #calculo la suma de las operaciones
            if cli.transaccion.upper() == "RETIRAR" :
                suma_retiros +=cli.cantidad_retirar
                if cli.edad < edad_minima_retiro :
                    edad_minima_retiro = cli.edad
            else:
                suma_consignaciones += cli.cantidad_consignar
                if cli.edad < edad_minima_consignacion :
                    edad_minima_consignacion = cli.edad
        else:
           # cola_info.append(cola_general[index].nombre)
            cola_info.append(cli.nombre)
            if cli.edad < edad_minima_info :
                edad_minima_info = cli.edad


    if edad_minima_consignacion == 99 :
        edad_minima_consignacion = -1
    if edad_minima_retiro == 99 :
        edad_minima_retiro = -1
    if edad_minima_info == 99 :
        edad_minima_info = -1
    



    #list comprehention + notation expression, aca no seria cola_caja sino la lista general
    #edad_minima_consignacion = [cli for cli in cola_caja if cli.transaccion == "CONSIGNAR" and cli.fila_interes == "CAJA"]
    #edad_minima_consignacion.sort(key=get_edad)

    #suma_consignaciones =  sum(c.cantidad_consignar for c in edad_minima_consignacion)
    #edad_minima_consignacion = edad_minima_consignacion[0].edad


    #edad_minima_retiro =  [cli for cli in cola_caja if cli.transaccion == "RETIRAR" and cli.fila_interes == "CAJA"]
    #edad_minima_retiro.sort(key=get_edad)

    #suma_retiros = sum(c.cantidad_retirar for c in edad_minima_retiro)
    #edad_minima_retiro = edad_minima_retiro[0].edad

    #cola_info.sort(key= get_edad)
    #edad_minima_info = cola_info[0].edad

    
    return cola_caja, cola_info, suma_retiros, suma_consignaciones, edad_minima_retiro, edad_minima_info, edad_minima_consignacion

"""
NO PEDIR DATOS CON LA FUNCIÓN input(), NO COLOCAR CÓDIGO FUERA DE LAS FUNCIONES QUE USTED CREE
Esta línea de código que sigue, permite probar si su ejercicio es correcto
Por favor NO ELIMINARLA, NO MODIFICARLA
"""
#pruebas_codigo_estudiante(sede_bancaria)

#test data
colaGeneral = []
colaGeneral.append(cliente("nombre3",14,2000,"CAJA","RETIRAR",1500,0))
colaGeneral.append(cliente("nombre2",11,2000,"CAJA","RETIRAR",1000,0))

colaGeneral.append(cliente("nombre5",16,500,"CAJA","CONSIGNAR",0,1501))
colaGeneral.append(cliente("nombre4",14,0,"CAJA","CONSIGNAR",0,1000))
colaGeneral.append(cliente("nombre8",13,0,"CAJA","CONSIGNAR",0,1000))

colaGeneral.append(cliente("nombre89",20,1,"INFO","NINGUNA",0,0))
colaGeneral.append(cliente("nombre1",12,1000,"INFO","NINGUNA",0,0))
colaGeneral.append(cliente("nombre6",17,1,"INFO","NINGUNA",0,0))
colaGeneral.append(cliente("nombre7",19,1,"INFO","NINGUNA",0,0))
colaGeneral.append(cliente("nombre88",20,1,"INFO","NINGUNA",0,0))

#sumas
s = sum(c.dinero_cuenta_bancaria for c in colaGeneral )
sumaConsiganciones = sum(c.cantidad_consignar for c in colaGeneral if c.transaccion == "CONSIGNAR" and c.fila_interes =="CAJA")
sumaRetiros= sum(c.cantidad_retirar for c in colaGeneral if c.transaccion == "RETIRAR" and c.fila_interes =="CAJA")

#obtener las edades minimas
edad_min_consigna = min(c.edad for c in colaGeneral if c.transaccion == "CONSIGNAR" and c.fila_interes =="CAJA")
edad_min_retira= min(c.edad for c in colaGeneral if c.transaccion == "RETIRAR" and c.fila_interes =="CAJA")
edad_min_info= min(c.edad for c in colaGeneral if c.transaccion == "NINGUNA" and c.fila_interes =="INFO")

#proyectar los nombres 
cola_consignar = list((c for c in colaGeneral if c.transaccion == "CONSIGNAR" and c.fila_interes =="CAJA"))
cola_consignar = list(map(lambda c: (c.nombre),cola_consignar))


sede_bancaria(colaGeneral)
