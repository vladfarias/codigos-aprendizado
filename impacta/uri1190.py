caractere = input().upper()

matriz = []
soma = 0
cont = 0
for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
        
        if j > i and j + i >= 12 :
            soma += linha[j]
            cont += 1

    matriz.append(linha)

if caractere == 'S':
    print(f'{soma:.1f}')
elif caractere == 'M':
    print(f'{(soma / cont):.1f}')
