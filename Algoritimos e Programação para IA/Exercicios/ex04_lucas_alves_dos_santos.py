def questao(int:int):
    print(f'''
    ------------------------------------------
                   Questão: {int}
    ------------------------------------------''')

questao(1)

def idade(idade:int):
    if idade < 0:
        print("Idade inválida.")
    elif idade <12:
        print("Criança.")
    elif idade >=12 and idade <= 17:
        print("Adolescente.")
    elif idade >= 18 and idade <= 59:
        print("Adulto")
    else:
        print("Idoso")

while True:
    try:
        age = int(input("Digite sua idade: "))

    except ValueError:
        print("Digite a idade como número inteiro, Ex: 1, 5..: ")
    else:
        idade(age)
    break

questao(2)

def retorna_maior(b:int,a:int):
    lista = []
    lista.append(a)
    lista.append(b)
    print(f"O maior número é: {max(lista)}")
    

while True:
    try:
        a = int(input("Digite um número para comparação: "))
        b = int(input("Digite outro número para comparação: "))
    except ValueError:
        print("Digite um número inteiro Ex: (< -1  0 >:): ")
    else:
        retorna_maior(a,b)
    break

questao(3)

def desconto(valor:float,desconto:float):
        porcentagem = valor*desconto
        valor_desconto = valor - porcentagem
        return(valor_desconto)

def calc_desconto(valor:float):
    if valor <= 100:
        print(f"O valor do produto com desconto é: {desconto(valor,0.05)}")
    elif valor > 100 and valor <= 500:
        print(f"O valor do produto com desconto é: {desconto(valor,0.10)}")
    else:
        print(f"O valor do produto com desconto é: {desconto(valor,0.15)}")

while True:
    try:
        valor = float(input("Digite o valor do produto: "))
    except ValueError:
        print("Digite o valor de um produto válido. Ex: (10.00, 10.50 ...): ")
    else:
        calc_desconto(valor)
    break
        

questao(4)
import math
def calc_hipotenusa(b:int,c:int):
    a = math.sqrt((math.pow(b,2) + math.pow(c,2)))
    print(f"O valor inteiro da hipotenusa é: {int(a)}")
while True:
    try:
       b = int(input("Digite o primeiro cateto: "))
       c = int(input("Digite o segundo cateto: "))
    except ValueError:
        print("Digite um valor inteiro.")
    else:
        calc_hipotenusa(b,c)
    break

questao(5)

def eh_triangulo(a,b,c):
    if abs(b-c) < a < a+b :
        return True
    elif abs(a-c) < b < a+c:
        return True
    elif abs(a-b) < c < a+b:
        return True
    else:
        return False

while True:
    try:
        a = int(input("Digite o valor do primeiro lado: "))
        b = int(input("Digite o valor do segundo lado: "))
        c = int(input("Digite o valor do terceiro lado: "))
    except ValueError:
        print("Digite um número")
    else:
        print(eh_triangulo(a,b,c))
    break

questao(6)

def valida_z():
    print("Iniciando função")
    x = 2
    z = 1
    if x > z:
        print("Verdadeiro")
        if x > 10:
            z = 10
        else:
            z = 20
    else:
        z = 30
    print(z)
valida_z()

questao(7)

def eh_par(numero):
    if numero%2 == 0:
        print(" O numero é par")
    else:
        print("O número é impar")

numero = int(input("Digite um número inteiro: "))
eh_par(numero)

questao(8)


def esta_aprovado(nota:int,frequencia:int):
    if nota >= 7 and frequencia >= 75:
        print("Aluno aprovado")
    else:
        print("Aluno reprovado")

nota = int(input("Digite a nota do aluno: "))
frequencia = int(input("Digite a frequência do aluno: "))

esta_aprovado(nota,frequencia)