def questao(int:int):
    print(f'''
    ------------------------------------------
                   Questão: {int}
    ------------------------------------------''')

questao(1)

def conta_ate_dez():
    for i in range(1,11):
        print(i)
conta_ate_dez()

questao(2)

def lista_ate_dez():
    lista = []
    for i in range(1,11):
        lista.append(i)
    print(lista)

lista_ate_dez()

questao(3)

def conjunto_ate_dez():
    conjunto = set()
    for i in range(1,11):
        conjunto.add(i)
    print(conjunto)

conjunto_ate_dez()

questao(4)

def tupla_ate_dez():
    tupla = ()
    for i in range(1,11):
         tupla = tupla + (i,)
    print(tupla)

tupla_ate_dez()

questao(5)

def inv_ate_dez():
    for i in range(10,0,-1):
        print(i)

inv_ate_dez()

questao(6)

def conta_ate_cem():
    for i in range(1,101,1):
        if i%2 == 0:
            print(i)

conta_ate_cem()

questao(7)

def soma_serie1(a,b):
    total = 0
    for a in range(a,b+1):
        total+=a
    print(f"O resultado da soma é: {total}")

def soma_serie2(a:int,b:int):
    qtd_termos = b-a+1
    total = (a+b)*qtd_termos//2
    print(f"O resultado da soma é: {total}")


while True:
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    if a < b:
        soma_serie1(a,b)
        soma_serie2(a,b)
        break
    else:
        print("O primeiro número deve ser menor que o segundo")

# Na minha opinião a diferença entre os dois é que um precisa fazer um looping e ir somando um a um, enquanto o outro é uma operação matemática que já faz o que precisa direto, sem a necessidade de um looping, quase como se estivesse fazendo 1+1

questao(8)

def fatorial(n):
    total = 1
    for i in range(n,0,-1):
        total*=i
    print(total)

while True:
    try:
        n = int(input("Digite o fatorial: "))
    except ValueError:
        print("Digite um número inteiro válido: ")
    else:
        fatorial(n)
    break

questao(9)

def fib(n):
    anterior = 0
    atual = 1
    for i in range(2,n+1,1):
        proximo = anterior + atual
        anterior = atual
        atual = proximo
        i+=1
    return atual

while True:
    try:
        n = int(input("Digite o fibonacci: "))
    except ValueError:
        print("Digite um número inteiro válido: ")
    else:
        print(fib(n))
    break 

questao(10)

def list_fib_n(n):
    lista = []
    for i in range(0,n,1):
        fibonacci = fib(i)
        lista.append(fibonacci)
    print(lista)

while True:
    try:
        n = int(input("Digite o fibonacci: "))
    except ValueError:
        print("Digite um número inteiro válido: ")
    else:
        list_fib_n(n)
    break 

