#  GEEK UNIVERSITY - Programação em Python do básico ao avançado
#  EXERCÍCIO 10 LISTA  13
"""Receba o nome de um arquivo de entrada e outro de saída. A entrada contém cidades em 
cada linha (ocupando 40 caracteres) e o seu número de habitantes. O programa deve ler a 
entrada e gerar um arquivo com a cidade mais populosa e o número de habitantes."""

print(f'{"--"}' * 100)
print('Se o arquivos não estiverem em:\nC:\\Users\\Vlad\\PycharmProjects\\guppe\n'
      'Por favor, informe todo o caminho')
print(f'{"--"}' * 100, '\n')

arq1 = input('Digite o nome ou o caminho do 1° arquivo:\n')
arq2 = input('Digite o nome ou o caminho do 2° arquivo:\n')

try:
    with open(arq1, 'r', encoding='utf-8') as entrada, open(arq2, 'w', encoding='utf-8') as saida:
        linhas = entrada.readlines()
        pop = 0

        for linha in linhas:
            li = linha.split(" ")
            ultimo = int(li[-1].strip('\n'))

            if pop < ultimo:
                pop = ultimo
                cidade = linha

        #  populosa = " ".join(cidade)
        saida.write(cidade)

except FileNotFoundError as erro:
    print(f'O seguinte erro foi identificado: {erro}')
