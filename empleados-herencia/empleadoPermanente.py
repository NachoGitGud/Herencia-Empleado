#!/usr/bin/python3

class EmpleadoPermanente:
    def __init__(self, nombre, apellido, dni, salario, antiguedad):
        self.antiguedad = antiguedad
        super().__init__(nombre, apellido, dni, salario)

    def calcular_comision(self):
        comision = self.salario * self.antiguedad / 100
        return comision
