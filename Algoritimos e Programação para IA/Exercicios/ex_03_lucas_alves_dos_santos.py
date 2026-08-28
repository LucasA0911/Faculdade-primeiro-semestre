print("--------------------------------------------------------------")
print("Questão 01")
print("--------------------------------------------------------------")

def escreva_ola():
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

def soma(a:int,b:int):
    return f"O resultado da soma é: {a+b}"

print(soma(10,5))
print(soma(15,5))

def subtracao(a:int,b:int):
    return f"O resultado da subtração é: {a-b}"

print(subtracao(20,5))
print(subtracao(15,5))

def multiplicacao(a:int,b:int):
    return f"O resultado da multiplicação é: {a*b}"

print(multiplicacao(10,5))
print(multiplicacao(10,10))

def divisao(a:int,b:int):
    return f"O resultado da divisão é: {a/b}"

print(divisao(10,5))
print(divisao(25,5))
#--------------------------------------------------------------

print("--------------------------------------------------------------")
print("Questão 04")
print("--------------------------------------------------------------")

def validar_usuario(nome:str,idade:int):  
    if len(nome) > 3 and  18 <= idade <= 100:
       return True
    else: 
        return False

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

def celsius_para_fahrenheit(celsius):
    return f"{(celsius * 9/5) + 32:.2f}Fº"

def fahrenheit_para_celsius(fahrenheit):
    return f"{(fahrenheit -32) * 5/9:.2f}Fº"

celsius = int(input("Insira a temperatura em Cº: "))
fahrenheit = int(input("Insira a temperatura em Fº: "))

print(celsius_para_fahrenheit(celsius))
print(fahrenheit_para_celsius(fahrenheit))