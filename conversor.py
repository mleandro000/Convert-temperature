# uso do argv para capturar entradas de uma função

from sys import argv   
from sys import exit # por padrão se um progama deu certo a saide dele é 0

MEDIDAS_VALIDAS = ["fahrenheit","celcius","kelvin"]
CONVERSAO_PARA_CELCIUS ={
    "celcius": lambda x: x,
    "fahrenheit": lambda x: (x - 32) * 5 / 9,
    "kelvin": lambda x: x - 273.15
}

CONVERTE_DE_CELCIUS_PARA_OUTRAS = {
    "celcius": lambda x: x,
    "fahrenheit": lambda x: (x * 9 / 5) + 32,
    "kelvin": lambda x: x + 273.15
}

def get_flag(flag): # a flag é a entrada que eu quero pegar 
    """retorna o valor de uma flag ou none"""
    total_argv = len(argv)
    i = 0
    while i < total_argv - 1:  # duvida porque eu não posso pegar o  ultimo argumento do conjunto de strings ou elementos
        argumento_atual = argv[i]
        if argumento_atual == flag:
            return argv[i+1]
        i +=1



entrada = get_flag("--entrada")
if not entrada:
    print("Você não passou entrada") 
    exit(1) #padronização de exits
if entrada not in MEDIDAS_VALIDAS:
    print("A entrada não está dentro de:", MEDIDAS_VALIDAS)
    exit(1)

saida = get_flag("--saida")
if not saida:
    print("Você não passou a saida")
    exit(1)
if saida not in MEDIDAS_VALIDAS:
    print("A saida não esta dentro de:", MEDIDAS_VALIDAS )
    exit(1)

numero = get_flag("--numero")
if not numero:
    print("Você não passou um numero")
    exit(1)
if not numero.isdigit():
    print("Você não digitou um número")
    exit(1)
#eu já tenho todas as entradas esperadas e suas validações
numero = float(numero)


em_celcius = CONVERSAO_PARA_CELCIUS[entrada](numero)
resultado = CONVERTE_DE_CELCIUS_PARA_OUTRAS[saida](em_celcius)

print(resultado)