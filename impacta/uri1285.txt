# Primeira versão URI 1285 - Numeros diferentes

def repetido(num):
    for n in num:
        if num.count(n) > 1:
            return True
    return False


while True:
    try:
        inicio = 0
        fim = 5001
        while inicio < 1 or fim > 5000:
            inicio, fim = input('i nicio e fim').split()
            inicio = int(inicio)
            fim = int(fim)

        cont = 0
        numero = inicio
        while numero <= fim:
            if not repetido(str(numero)):
                cont += 1
                numero += 1
            else:
                numero += 1

        print(cont)

    except EOFError:
        break
