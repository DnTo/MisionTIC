"""
1. Write a Python class named Circle constructed by a radius and two methods which will 
compute the area and the perimeter of a circle.

2. Write a Python class named Rectangle constructed by a length and width and a method 
which will compute the area of a rectangle

3. Crear una clase Inventario, que tenga un código de referencia, unas unidades y un método 
para retirar y agregar unidades a la referencia. Debe tener un método para consultar las 
unidades restantes
"""
import math

class Circle:
	def __ini__(radius):
		self.radius=radius

	def calculateArea(self):
		return math.pi * self.radius*self.radius
		
	def calculatePerimeter(self):
		return 2*math.pi*radius

class Rectangle:
	def __init__(self,w,l):
		self.width = w
		self.length = l

	def calculateArea(self):
		return self.w * self.l


class Inventory:
	__units = 0
	def __init__(self,reference):
		self.reference = reference
		self.__units = 0

	def addUnits(self,num):
		self.__units += num 

	def removeUnits(self,num):
		self.__units-=num

	def queryUnits(self):
		return self.__units


inventory = Inventory("sdsd")

inventory.addUnits(5)
print(inventory.queryUnits())
inventory.removeUnits(3)
print(inventory.queryUnits())


