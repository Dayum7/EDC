def lista_fatores_primos():

    resto_divisao = int(input("Digite um numero inteiro maior que 1: \nR:"))

    fator_primo = 2
    while resto_divisao != 1:
        expoente = 0
        while resto_divisao%fator_primo == 0:
            resto_divisao = resto_divisao / fator_primo
            expoente = expoente + 1

        if expoente != 0:
            print("fator primo - %d^%d" %(fator_primo, expoente))

        fator_primo = fator_primo + 1

lista_fatores_primos()