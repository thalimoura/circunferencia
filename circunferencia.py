print("circunferencia")

pi = 3.14159265

def calcular_area(raio):
    area = pi * (raio ** 2)
    return area

raio = float(input("digite o raio: "))

area_calculada = calcular_area(raio)

print("a area da circunferencia é: ", area_calculada)