num = int(input('digite um valor: '))

maior = num
menor = num

cc = str(input('digite n para parar ou s: '))


    num = int(input('digite um valor: '))

    if num > maior:
        maior = num
    
    if maior < menor:
        menor = num

    cc = str(input('digite n para parar ou s: '))

    print('o maior valor é: {}' .format(maior))