def check_linha_coluna(matriz, li, col):
    check_col = 0
    check_li = 0
    for k in range(9):

        if matriz[li][col] == matriz[li][k]:
            check_li += 1
        if matriz[li][col] == matriz[k][col]:
            check_col += 1
    return check_col == 1 and check_li == 1


def check_regioes(matriz, li, col):
    cont = 0

    if  (0 <= li < 3) and (0 <= col < 3):
        for k in range(3):
            for m in range(3):
                if matriz[li][col]== matriz[k][m]:
                    cont += 1
        return cont == 1

    elif (0 <= li < 3) and (3 <= col < 6):
        for k in range(3):
            for m in range(3, 6):
                if matriz[li][col]== matriz[k][m]:
                    cont += 1
        return cont == 1

    elif (0 <= li < 3) and (6 <= col < 9):
        for k in range(3):
            for m in range(6, 9):
                if matriz[li][col]== matriz[k][m]:
                    cont += 1
        return cont == 1

    elif (3 <= li < 6) and (0 <= col < 3):
        for k in range(3, 6):
            for m in range(3):
                if matriz[li][col]== matriz[k][m]:
                    cont += 1
        return cont == 1

    elif (3 <= li < 6) and (3 <= col < 6):
        for k in range(3, 6):
            for m in range(3, 6):
                if matriz[li][col]== matriz[k][m]:
                    cont += 1
        return cont == 1

    elif (3 <= li < 6) and (6 <= col < 9):
        for k in range(3, 6):
            for m in range(6, 9):
                if matriz[li][col]== matriz[k][m]:
                    cont += 1
        return cont == 1

    elif (6 <= li < 9) and (0 <= col < 3):
        for k in range(6, 9):
            for m in range(3):
                if matriz[li][col]== matriz[k][m]:
                    cont += 1
        return cont == 1

    elif (6 <= li < 9) and (3 <= col < 6):
        for k in range(6, 9):
            for m in range(3, 6):
                if matriz[li][col]== matriz[k][m]:
                    cont += 1
        return cont == 1

    else:
        for k in range(6, 9):
            for m in range(6, 9):
                if matriz[li][col]== matriz[k][m]:
                    cont += 1
        return cont == 1


def sudoku(matriz):
    for i in range(9):
        for j in range(9):
            atende =  check_linha_coluna(matriz, i, j) and check_regioes(matriz, i, j)
            if not atende:
                return False
    return True


n = int(input())
instancia = 0

while instancia < n:

    entradas = []
    for i in range(9):
        entradas.append([int(num) for num in input().split()])

    instancia += 1
    if sudoku(entradas):
        print(f'Instancia {instancia}\nSIM\n')
    else:
        print(f'Instancia {instancia}\nNAO\n')
