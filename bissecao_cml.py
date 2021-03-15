'''
Documentação:

Ao digitar o comando no terminal deve-se colocar:
python (ou python3) nomedoarquivo.py 'equação f(x)' precisao valor_do_intervalo_inicial valor_do_intervalo_final 
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

def bissecao(x_inicial, x_final):
    '''
    Método da Bisseção: x = (x_inicial + x_final)/2 
    Parâmetros: x_inicial (float), x_final (float)
    Retorno: possível raíz (float)
    '''
    x_i = (x_inicial + x_final)/2
    
    return x_i

# Entrada de Variáveis
precisao = float(sys.argv[2])
x_inicial = float(sys.argv[3])
x_final = float(sys.argv[4])

# Vetores
vetor_xi = [x_inicial]                                   # Vetor para salvar os valores testados
vetor_funcao = [funcao(x_inicial)]                       # Vetor para salvar a função em cada aplicação
vetor_contador = [0]                                     # Vetor para contar o número de aplicações

# Lógica Principal
contador = 0                                             # Contador do número de aplicações necessárias

if funcao(x_inicial)*funcao(x_final) < 0:

    while (abs(x_final - x_inicial)/2 > precisao):
        xi = bissecao(x_inicial, x_final)
        contador += 1                                    # Aumentando o contador

        # Adicionando as coordenadas nos vetores vetores
        vetor_xi.append(xi)
        vetor_funcao.append(funcao(xi))
        vetor_contador.append(contador)

        if funcao(xi) == 0:
            print('\nA raiz é %5.7f' %xi)
            break

        elif contador == 100:
            break 

        else:
            if funcao(x_inicial)*funcao(xi) < 0:
                x_final = xi
            else:
                x_inicial = xi

    # Saindo do loop
    print('\nCálculo encerrado após', contador,'aplicações.')
    print('O valor final da raiz é %5.7f' %xi)

else:
    contador = 0
    print('\nNão há raiz nesse intervalo ou há mais de uma raiz no intervalo')

# Gráfico das aproximações
plt.plot(vetor_contador, vetor_xi, 'r-')
plt.title('Evolução da aproximação da raiz')
plt.xlabel('Aplicações')
plt.ylabel('Aproximação')
plt.grid(True)
plt.show()