dic = {'domingo': 1, 'segunda': 2, 'terca': 3, 'quarta': 4,
       'quinta': 5, 'sexta': 6, 'sabado': 7}

dia_compra = input('Digite o dia da compra:')

prazo = 7
while prazo < 0 or prazo > 6:
 prazo = int(input('digite o prazo:'))


n_dia_compra = dic[dia_compra]

entrega = n_dia_compra + prazo

if prazo == 0:
    print('chega hoje!')
