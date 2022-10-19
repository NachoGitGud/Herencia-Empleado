#!/usr/bin/python3

class EmpleadoEventual:
    def __init__(self, nombre, apellido, dni, salario, ventas):
        self.ventas = ventas
        super().__init__(nombre, apellido, dni, salario)

    def calcular_comision(self):
        total_ventas = 0
        for una_venta in self.ventas:
            total_ventas = total_ventas + una_venta

        # O bien:
        # total_ventas = sum(self.ventas)
        
        porcentaje_comision = 0.05
        comision = total_ventas * porcentaje_comision
        return comision