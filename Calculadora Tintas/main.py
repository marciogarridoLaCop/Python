# Programa para cálculo de volume de tintas para comodos
#
from calculadora import Calculadora
from comodo import Comodo

calc = Calculadora()
comodo = Comodo(float(input("Digite o valor da largura ")),
                float(input("Digite o valor da profundidade ")))
print( "A área das paredes é de : ",
       calc.calcular_area_paredes(comodo))
print( "A área do teto é de : ",
       calc.calcular_area_teto(comodo))
print( "A litragem de tinta necessária é de :", round(calc.calcular_litragem_necessaria(),3))