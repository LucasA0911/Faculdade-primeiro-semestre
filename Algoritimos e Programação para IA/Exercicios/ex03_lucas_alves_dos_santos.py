print("--------------------------------------------------------------")
print("Questão 01")
print("--------------------------------------------------------------")

def escreve_ola():
    print("Olá exercicio 3")
#-----------------------------------------

print("--------------------------------------------------------------")
print("Questão 02")
print("--------------------------------------------------------------")

def a(a:bool,b:bool):
    return a and b
print(a(True,False))

def b(a:bool,b:bool):
    return a or b
print(b(True,False))

def c(a:bool):
    return not a
print(c(True))

def d(b:bool,c:bool):
    return b and c
print(d(False,False))

def e(a:bool,b:bool,c:bool):
    return a or b and c
print(e(True,False,True))
#-----------------------------------------------

print("--------------------------------------------------------------")
print("Questão 03")
print("--------------------------------------------------------------")

def soma(a,b):
    return f"O resultado da soma é: {a+b}"
for i in range(2):
    a = float(input("Digite o primeiro número da soma: "))
    b = float(input("Digite o segundo número da soma: "))
    print(soma(a,b))

def subtracao(a,b):
    return f"O resultado da subtração é: {a-b}"
for i in range(2):
    a = float(input("Digite o primeiro número da subtração: "))
    b = float(input("Digite o segundo número da subtração: "))
    print(subtracao(a,b))

def multiplicacao(a,b):
    return f"O resultado da multiplicação é: {a*b}"
for i in range(2):
    a = float(input("Digite o primeiro número da multiplicação: "))
    b = float(input("Digite o segundo número da multiplicação: "))
    print(multiplicacao(a,b))

def divisao(a,b):
    return f"O resultado da divisão é: {a/b}"
for i in range(2):
    a = float(input("Digite o primeiro número da divisão: "))
    b = float(input("Digite o segundo número da divisão: "))
    print(divisao(a,b))
#--------------------------------------------------------------

print("--------------------------------------------------------------")
print("Questão 04")
print("--------------------------------------------------------------")

def validar_usuario(nome:str,idade:int):  
     return len(nome) >= 3 and  18 <= idade <= 100

print(validar_usuario("Lucas",26))
print(validar_usuario("Art", 100))
#-------------------------------------------------------------

print("--------------------------------------------------------------")
print("Questão 05")
print("--------------------------------------------------------------")

lista = [1,2,3,4,5,6,7,8,9,10]

print(f"A quantidade de elementos na lista é: {len(lista)}")
print(f"O maior valor da lista é: {max(lista)}")
print(f"O menor valor da lista é: {min(lista)}")
print(f"A soma dos valores da lista é: {sum(lista)}")
print(f"A média dos valores da lista é: {sum(lista)/len(lista)}")
print(f"O primeiro elemento é: {lista[0]}")
print(f"O ultimo elemento da lista é: {lista[-1]}")
print(f"Os três primeiros elementos são: {lista[:3]}")
print(f"Os três ultimos elementos são: {lista[-3:]}")
print(f"Os números pares são: {lista[1::2]}")
lista[0:2] = [1,0]
print(f"Os números atualizados da lista são: {lista[0:2]}")
lista.append(11)
lista.append(12)
print(f"A lista com os novos números é: {lista}")
lista.pop(-1)
print(f"A lista atualizada após todas as operações: {lista}")
#-------------------------------------------------------------------

print("--------------------------------------------------------------")
print("Questão 06")
print("--------------------------------------------------------------")

produto = ("Notebook",3500.00,10,"informatica")
nome,preco,quantidade,categoria = produto

print(f"{nome}, {preco}, {quantidade}, {categoria}")

def valor_estoque(item):
    quantidade = item[2]
    valor = item[1]
    return f"O valor total do estoque é: {quantidade*valor}"

print(valor_estoque(produto))
#---------------------------------------------------------------

print("--------------------------------------------------------------")
print("Questão 07")
print("--------------------------------------------------------------")

ponto =(10,20,30)
x,y,z = ponto
def soma(x,y,z):
    return f"A soma das coodernadas é: {x+y+z}"
print(soma(x,y,z))
#-----------------------------------------------------------------------------

print("--------------------------------------------------------------")
print("Questão 08")
print("--------------------------------------------------------------")

aluno = {
    "nome":"Lucas",
    "idade":27,
    "curso":"TIA",
    "nota1":10.0,
    "nota2":8.5
}
def calcular_media(aluno):
    return (aluno["nota1"] + aluno["nota2"])/2
print(calcular_media(aluno))
aluno["media"] = calcular_media(aluno)

nome,idade,curso,nota1,nota2,media = aluno.values()
print(f"{nome}, {idade}, {curso}, {nota1}, {nota2}, {media}")
#----------------------------------------------------------------------

print("--------------------------------------------------------------")
print("Questão 09")
print("--------------------------------------------------------------")

def celsius_para_fahrenheit(celsius:int):
    return f"{(celsius * 9/5) + 32:.2f}Fº"

def fahrenheit_para_celsius(fahrenheit:int):
    return f"{(fahrenheit -32) * 5/9:.2f}Cº"

celsius = float(input("Digite a temperatura em Cº: "))
fahrenheit = float(input("Digite a temperatura em Fº: "))
print(celsius_para_fahrenheit(celsius))
print(fahrenheit_para_celsius(fahrenheit))

print("--------------------------------------------------------------")
print("Questão 10")
print("--------------------------------------------------------------")

viagem = ("Rio de Janeiro", 5, "ônibus", 850.00)

cidade_destino, dias, transporte, valor = viagem

print(viagem)
print(f"A quantidade de elementos na tupla é de: {len(viagem)}")
print("ônibus" in viagem)

viagem_nova = viagem + ("Hotel",)

cidade_destino, dias, transporte, valor, hospedagem = viagem_nova

print(viagem_nova)

print("--------------------------------------------------------------")
print("Questão 11")
print("--------------------------------------------------------------")

def produto(nome:str, categoria:str, preco:float,qtd_estoque:int, codigo_produto:int):
    item = {
        "nome":nome,
        "categoria":categoria,
        "preco":preco,
        "qtd_estoque":qtd_estoque,
        "codigo_produto":codigo_produto,
        "valor_estoque":preco*qtd_estoque
    }
    return item
nome = input("Digite o nome do produto: ")
categoria = input("Digite a categoria do produto: ")
preco = float(input("Digite o preço do produto no estilo XX.XX: "))
qtd_estoque = int(input("Digite a quatidade do produto: "))
codigo_produto = int(input("Digite o código do produto: "))

produto = produto(nome,categoria,preco,qtd_estoque,codigo_produto)
print(produto)
print(produto["nome"])
print(produto["categoria"])
print(produto["preco"])
print(produto["qtd_estoque"])
print(produto["codigo_produto"])
print(produto["valor_estoque"])

print("--------------------------------------------------------------")
print("Questão 12")
print("--------------------------------------------------------------")

def area_circulo(diametro:float):
    area = 3.14 * pow(raio_circulo(diametro),2)
    return area

def raio_circulo(diametro:float):
    raio = diametro/2
    return raio

print(f"{area_circulo(30)}cm²")
print(f"{area_circulo(50)}cm²")
