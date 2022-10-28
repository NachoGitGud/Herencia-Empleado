#!/usr/bin/python3

class EmpleadoFundamental:
    def __init__(self, nombre, apellido, dni, salario):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.salario = salario
    
    def calcular_ingreso_total(self):
        ingreso_total = self.salario + self.calcular_comision()
        return ingreso_total

    def coincide(self, texto_a_buscar):
        if texto_a_buscar in self.nombre or texto_a_buscar in self.apellido:
            return True
        else:
            return False
    
