# ## Questão 1
#
# Você foi contratado pela seleção brasileira para fazer uma análise sobre as seleções adversárias. Sua primeira tarefa
# consiste em realizar uma contagem de quantos jogadores possuem a altura máxima.
#
# ### Exemplo
#
# Para a entrada:
#
# ```
# [180, 166, 170, 180]
# ```
#
# A saída deve ser:
#
# ```
# 2
# ```
#
# Isso porque existem dois jogadores com altura máxima (180).
#
# Para obter a nota máxima dessa questão, deve-se utilizar apenas um ``for`` e nenhuma função pronta do Python.

def q1(heights):
    max = 0
    maxnum = 1

    for i in heights:
        if i > max:
            max = i
        elif i == max:
            maxnum += 1
        else:
            pass

    return maxnum




if __name__ == '__main__':
    print(q1([180, 166, 170, 180]))
