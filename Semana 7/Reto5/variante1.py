#NO ELIMINAR LAS SIGUIENTES IMPORTACIONES, sirven para probar tu código en
#consola, y el funcionamiento del módulo csv respectivamente
#from pruebas import pruebas_codigo_estudiante
import csv
import os
"""NOTAS: 
    -PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
    -LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO
"""


"""Inicio espacio para programar funciones propias"""
#En este espacio podrás programar las funciones que deseas usar en la función
#solución (ES OPCIONAL)


"""Fin espacio para programar funciones propias"""

def solucion():
    #ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN
    #EL ENUNCIADO.
    resultados = [["Fecha","Concepto"]]
    date_lowest = ''
    lowest_value = 0.0
    date_highest = ''
    highest_value = 0.0

    
    with open('analisis_archivo.csv','w',newline="") as resultCSV:
        writer = csv.writer(resultCSV,delimiter="\t")

        with open("TSLA.csv",newline="") as teslaCSV:
            reader = csv.reader(teslaCSV,delimiter=",")
            cont = 0 
            next(reader)
            row = next(reader)
           
            lowest_value = float(row[3])
            highest_value = float(row[2])

            teslaCSV.seek(0)
            for row in reader:
                if cont != 0:
                    valorCierre = float(row[4])
                    #valor-fecha mayor y menor
                    if(float(row[2]) >= highest_value):
                        highest_value = float(row[2])
                        date_highest = row[0]
                    if(float(row[3]) <= lowest_value):
                        lowest_value = float(row[3])
                        date_lowest = row[0]


                    if valorCierre >= 600:
                        resultados.append([row[0],"MUY ALTO"])
                    elif valorCierre >= 500:
                        resultados.append([row[0],"ALTO"])
                    elif valorCierre >= 300:
                        resultados.append([row[0],"MEDIO"])
                    elif valorCierre >= 200:
                        resultados.append([row[0],"BAJO"])
                    else:
                        resultados.append([row[0],"MUY BAJO"])
                cont+=1
        writer.writerows(resultados)
            


    #crear archivo analisis_archivo.csv con tabs
    
    
    return date_lowest, lowest_value, date_highest, highest_value

"""
NO COLOCAR CÓDIGO FUERA DE LAS FUNCIONES QUE USTED CREE
Esta línea de código que sigue permite saber si su solución al ejercicio es correcto
Por favor NO ELIMINARLA, NO MODIFICARLA
"""
#pruebas_codigo_estudiante(solucion)

solucion()