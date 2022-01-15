from cgitb import text
import math

def ExtendedEuclid(n, B, calculo=False):
    a1, a2, a3 = 1, 0, n
    b1, b2, b3 = 0, 1, B
    
    if(calculo):
        print("Q\tA1\tA2\tA3\tB1\tB2\tB3")
    q = None

    while(True):

        if(calculo):
            print("%s\t%s\t%s\t%s\t%s\t%s\t%s" % (q, a1, a2, a3, b1, b2, b3))

        if b3 == 0:
            return a3, None

        if b3 == 1:
            if b2 < 0:
                b2 = b2 + B
            return b3, b2

        q = math.floor(a3/b3)

        t1, t2, t3 = a1 - q*b1, a2 - q*b2, a3 - q*b3
        a1, a2, a3 = b1, b2, b3
        b1, b2, b3 = t1, t2, t3


def main():
    while(True):
        loop=1

        while(loop==1):
            n = int(input("Indique um numero:"))
            B = int(input("Indique o valor do modulo:"))
            if(B<=n):
               print("Erro: valor de modulo tem de ser o valor menor")
            else:
                loop=0


        tabela = ExtendedEuclid(n, B, True)
        print("MDC(%s, %s) = %s\nMultiplicativo Inverso= %s" % (n, B, tabela[0], tabela[1]))

        print("Pretende continuar? s ou n")
        text = input()
        if text=="n":
            break

main()
