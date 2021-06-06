import random
from persona import Persona 
#hacer una clase que se llame CuentaBancaria.
#artibutos:
# numero de la cuenta -> es aleatorio entre 1.000 y 10.000
# saldo
#m�todos:
# retirar
# depositar

#ejercicio: agregar condici�n que saque error si el saldo es negativo
# ok ejercicio: cobrar una comisi�n del 4 pesos por cada 1000 cuando el monto
# de la consignaci�n sea mayor a 10.000

#ejercicio opcional: crear una lista de cuentas y agregar la posibilidad de
#crear una cuenta nueva o eliminar una cuenta
 #cuando se vaya a retitar o a consignar, se debe ingresar el n�mero de la
 #cuenta

# ejercicio opcional: crear una clase persona y a la clase cuenta agregarle una
# persona pidi�ndole su c�dula.
#Hay que construir una lista de personas.  Si la persona no existe, se debe
#crear.
class Banco:
    def __init__(self):
         self.cuentas = []
         self.clientes = []

    def crearCuenta(self,cuenta):
        '''Creo una cuenta nueva y devuelvo el nro de cuenta '''
         # como es cuenta nueva puedo renovar el id altearotiamente hasta que
         # no exista
        while(self.cuentaIdYaExiste(cuenta)):
            self.__renovarIdCuentaNueva(cuenta)
        
        if(self.personaYaExiste(cuenta.titular)):#si la persona no existe
             self.cuentas.append(cuenta)
        else:   
            self.clientes.append(cuenta.titular)
            self.cuentas.append(cuenta)
        return cuenta.numeroCuenta

    def obtenerCuenta(self,numCuenta): #todos los metodos de abajo podrian  usar este metodo
        for index,element in enumerate(self.cuentas):
            if(element.numeroCuenta == numCuenta):
                return [index,element]
        return [-1] #no encontro la cuenta

    def cuentaIdYaExiste(self,cuenta):
        #verifico si el id ya existe
        yaExisteIdCuenta = False
        for index,element in enumerate(self.cuentas):
            if(element.numeroCuenta == cuenta.numeroCuenta):
                yaExiste = True
                break

    def eliminarCuenta(self,numCuenta):
        for element in self.cuentas:
            if(element.numeroCuenta == numCuenta):
                saldo = element.saldo
                self.cuentas.remove(element)
                return [True,saldo]
        return [False] #no encontro la cuenta

    def personaYaExiste(self,persona):
    #verifico si la persona ya existe
        existePersona = False
        for element in self.clientes:
            if(element.documento == persona.documento):
                existePersona = True
                return existePersona
        return existePersona
    
    def __renovarIdCuentaNueva(self,cuentaNueva):
        ''' Renuevo el id de la cuenta y devuelvo la cuenta'''
        cuentaNueva.numeroCuenta = random.randint(1000,10000)
        return cuentaNueva
        

class CuentaBancaria:
    def __init__(self,saldoInicial,persona):
        self.numeroCuenta = random.randint(1000,10000)
        if saldoInicial < 0 :
            raise ValueError("El valor no puede ser menor que 0")
        self.saldo = saldoInicial
        self.titular = persona
        self.transacciones = []

    def retirar(self, monto):
        if monto > self.saldo   :
            print("Fondos insuficientes")
        #elif monto>= 10000 and monto*1.004 > self.saldo: #4 x 1000
        #    print("Fondos insuficientes x 4x1000")
        else:
            self.saldo = self.saldo - monto #if monto <10000 else monto * 1.004 #4 x 1000 .  Normalmente el 4x100 se cobra
                                            #al retirar
            print("Retiro Exitoso")

    def consignar(self,monto):
        self.saldo = self.saldo + (monto if monto < 10000 else monto - (monto * 0.004)) #4 pesos por cada 1000 cuando el monto de la consignaci�n sea mayor a 10.000

    def consultarSaldo(self):
        print("Cuenta: ",self.numeroCuenta)
        print("Saldo: ",self.saldo)
        print("________________")



banco = Banco()
print("Bienvenido al banco XYZ.\n ")

while True:

    print("MENU\n\nADMINISTRACION:\n[CC] Crear una cuenta.\n[EC] Eliminar una cuenta\n[LC]  listar cuentas.\n[LP]  listar personas.\n\nCAJA: \n[S] consultar el saldo\n[R]  retiros\n[C] consignar\n ")
    
    operacion = input("Elja su opción: ").upper()
    if operacion == "S":
        print("CONSULTA DE SALDO")
        nroCuenta = int(input("Ingrese el numero de cuenta a consultar: "))
        consultaCuenta = banco.obtenerCuenta(nroCuenta)
        if consultaCuenta[0]!=-1 :
            consultaCuenta[1].consultarSaldo()
        else:
             print("No encontramos esa cuenta. Verifica los datos!.")


        


    elif operacion == "R":
        print("RETIRO DE SALDO")
        nroCuenta = int(input("Ingrese el numero de cuenta a retirar: "))
        consultaCuenta = banco.obtenerCuenta(nroCuenta)
        if consultaCuenta[0]!=-1 :
            monto = float(input("Ingrese el monto que quiere retirar: "))
            consultaCuenta[1].retirar(monto)
           
        else:
             print("No encontramos esa cuenta. Verifica los datos!.")

     
    elif operacion == "C":
        print("CONSIGNAR  SALDO")

        nroCuenta = int(input("Ingrese el numero de cuenta a CONSIGNAR: "))
        consultaCuenta = banco.obtenerCuenta(nroCuenta)
        if consultaCuenta[0]!=-1 :
            monto = float(input("Ingrese el monto que quiere consignar: "))
            consultaCuenta[1].consignar(monto)
            print("Consignación exitosa")
        else:
             print("No encontramos esa cuenta. Verifica los datos!.")
      
   
       
        
    #ADMON
    elif operacion == "CC":
          doc = input("Ingrese el documento del titular: ")
          persona = Persona(doc)
          saldoInicial = float(input("ingrese el saldo inicial de la cuenta: "))
          
          cuenta = CuentaBancaria(saldoInicial,persona)
          banco.crearCuenta(cuenta)
          
          print(f"Se ha creado correctamente la cuenta con Nro {cuenta.numeroCuenta} para el titular {doc}")
    elif operacion == "EC":
          nroCuenta = int(input("Ingrese el numero de cuenta a eliminar: "))
          resultado = banco.eliminarCuenta(nroCuenta)
          if resultado[0] :
              print(f"Cuenta eliminada con exito. Por favor pase por caja y reclame {resultado[1]}")
          else :
              print(f"Cuenta no existe, por favor verifique e intente nuevamente.")


    elif operacion == "LC":
          print(f"Listado cuentas activas en el banco")
          print(f"Titular  | NroCuenta  | Saldo ")
          for cuenta in banco.cuentas:
           print(f"{cuenta.titular.documento:5}    |   {cuenta.numeroCuenta:5}    | {cuenta.saldo:5} ")

    elif operacion == "LP":
          print(f"Listado Personas")
          print(f"Documento | Nombre")
          for persona in banco.clientes:
            print(f"{persona.documento:10}{persona.nombre:10}")
    else:
        print("Operación incorrecta")
    
    input("\n\npresione una tecla para continuar...")
    #cls
    print("\n"*5)

        