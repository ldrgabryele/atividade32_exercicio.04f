#Faça um programa que pergunte quanto você ganha por hora e
#o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no
#referido mês.

hrs = float(input("Digite o quanto você ganha por horas: "))
mes = float(input("Digite o número de horas trabalhadas no mês: "))

def salario (hrs,mes):
    valor = hrs * mes
    print(valor)

salario(hrs,mes)