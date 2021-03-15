'''
Documentação:

Ao digitar o comando no terminal deve-se colocar:
python (ou python3) nomedoarquivo.py 'equação f(x)' 'equação df(x)/dx' precisao valor_do_intervalo_inicial 
'''

# Biblioteca
import numpy as np
import sys
import matplotlib.pyplot as plt

# Funções
def funcao(x):
    """
    Digite em forma de string a sua função

    Parâmetros: x
    Retorno: y (float)
    """
    return eval(sys.argv[1])

def derivada(x):
    """
    Digite em forma de string a derivada da sua função

    Parâmetros: x
    Retorno: dy/dx (float)
    """
    return eval(sys.argv[2])

def Newton_Raphson(x):
    '''
    Método de Newton-Raphson: x = x0 - f(x0)/f'(x0)
    Variável de entrada: x (float)
    Saída: possível raíz (float)
    '''
    if derivada == 0:
        print ("Erro! Altere o ponto inicial e tente novamente.")
    else:
        return x - funcao(x)/derivada(x)

# Entrada de Variáveis
precisao = float(sys.argv[3])
x_inicial = float(sys.argv[4])

# Vetores
vetor_x = [x_inicial]                   # Vetor para salvar os valores testados
vetor_funcao = [funcao(x_inicial)]      # Vetor para salvar a função em cada aplicação
vetor_contador = [0]                    # Vetor para contar o número de aplicações

# Lógica Principal
x0, x1 = x_inicial, x_inicial           # Começamos pelo valor inicial
contador = 0                            # Contador do número de aplicações necessárias

while (abs(funcao(x1)) >= precisao):    # Enquanto a função for maior que o valor máximo admitido
    x1 = Newton_Raphson(x0)                     # Aplicando um passo no método de Newton-Raphson
    x0 = x1                             # Recurssão
    contador += 1                       # Aumentando o contador
    if contador == 100:
        break

    # Adicionando as coordenadas nos vetores vetores
    vetor_x.append(x1)
    vetor_funcao.append(funcao(x1))
    vetor_contador.append(contador)

# Saindo do loop
print('\nCálculo encerrado após', contador,'aplicações.')
print('Raiz encontrada é %5.7f' %x1)

# Gráfico das aproximações
plt.plot(vetor_contador, vetor_x, 'r-')
plt.title('Evolução da aproximação da raiz')
plt.xlabel('Aplicações')
plt.ylabel('Aproximação')
plt.grid(True)
plt.show()