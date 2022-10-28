#!/usr/bin/python3

from empleadoFundamental import EmpleadoFundamental

class EmpleadoPermanente(EmpleadoFundamental):
    def __init__(self, nombre, apellido, dni, salario, antiguedad):
        self.antiguedad = antiguedad
        super().__init__(nombre, apellido, dni, salario)

    def calcular_comision(self):
        comision = self.salario * self.antiguedad / 100
        return comision
        
    def mostrar_datos(self):
        texto = f"Nombre y apellido: {self.nombre} {self.apellido}\n"
        texto += f"DNI: {self.dni} - Salario: {self.salario}\n" 
        texto += f"Antigüedad: {self.antiguedad}\n"
        return texto   
