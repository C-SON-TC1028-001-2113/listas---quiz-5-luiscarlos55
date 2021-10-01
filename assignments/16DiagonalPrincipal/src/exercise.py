def matriz(lista):
    diagonal = []
    for i in range(len(lista)):
        diagonal.append(lista[i][i])
    return (diagonal)

def main():
    lista = []
    x = int(input(''))
    y = int(input(''))
    if x==y :
        for i in range(x):
            lista.append([])
            for j in range(y):
                n = int(input())
                lista[i].append(n)
        resultado = matriz(lista)
        print(resultado)
    else:
        print('La matriz no es cuadrada')

if __name__=='__main__':
    main()