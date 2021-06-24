#from pruebas import pruebas_codigo_estudiante#NOTA: PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE#ESPACIAL#LA CONSOLA TE DAR� INSTRUCCIONES SI PUEDES EVALUAR O NO TU C�DIGO#En este espacio podr�s programar las funciones que deseas usar en la funci�n#soluci�n (NO ES OBLIGATORIO CREAR OTRAS FUNCIONES)"""Inicio espacio para programar funciones propias"""#PUEDES PROGRAMAR CUANTAS FUNCIONES DESEES"""Fin espacio para programar funciones propias"""def traductor_a_espanol(mensaje_a_traducir):    #PROGRAMA AC� TU SOLUCI�N   
# #diccionario    
dictionary = { 'A':".-", 'B':"-...", 'C':"-.-.", 'D':"-..", 'E':".", 'F':"..-.", 'G':"--.", 'H':"....", 'I':"..", 'J':".---", 'K':"-.-", 'L':".-..", 'M':"--", 'N':"-.", 'O':"---", 'P':".--.", 'Q':"--.-", 'R':".-.", 'S':"...", 'T':"-", 'U':"..-", 'V':"...-", 'W':".--", 'X':"-..-", 'Y':"-.--", 'Z':"--..", } #return mensaje_traducido    return dictionary"""Esta l�nea de c�digo que sigue, permite probar si su ejercicio es correcto"""#NO ELIMINAR LA SIGUIENTE L�NEA DE C�DIGO#pruebas_codigo_estudiante(traductor_a_espanol)##
letters2Morse = { 'A':".-", 'B':"-...", 'C':"-.-.", 'D':"-..", 'E':".", 'F':"..-.", 'G':"--.", 'H':"....", 'I':"..", 'J':".---", 'K':"-.-", 'L':".-..", 'M':"--", 'N':"-.", 'O':"---", 'P':".--.", 'Q':"--.-", 'R':".-.", 'S':"...", 'T':"-", 'U':"..-", 'V':"...-", 'W':".--", 'X':"-..-", 'Y':"-.--", 'Z':"--..", }
morse2letters = {".-":'A',"-...":'B',"-.-.":'C',"-..":'D',".": 'E',"..-.":  'F', "--.":'G',      "....":  'H', "..":'I', ".---":'J', "-.-":'K', ".-..":'L', "--":'M', "-.":'N', "---":'O', ".--.":'P', "--.-":'Q', ".-.":'R', "...":'S', "-":'T', "..-":'U',"...-": 'V', ".--":'W', "-..-":'X', "-.--":'Y', "--..":'Z', "/":" " ,'"':""}
frase = "-. --- ... / .... .- -. / .--. .. -.-. .- -.. --- / -.. --- ... / -- --- ... --.- ..- .. - --- ..."
frase2 = ".... . -- --- ... / . -. -.-. --- -. - .-. .- -.. --- / ..- -. .- / .--. .-.. .- -. - .- / -. ..- -. -.-. .- / .- -. - . ... / ...- .. ... - .-"

frase3 = ".... --- .-.. .- / -- ..- -. -.. --- "
frasePhase1 = frase.split("/")
#obtengo todas las palabras

result = ""
for word in frasePhase1:   
	wordPhase1 = word.strip().split(" ")
	for letter in wordPhase1:
		result += morse2letters.get(letter.strip())
	result+=" "
	
print(result.strip())
