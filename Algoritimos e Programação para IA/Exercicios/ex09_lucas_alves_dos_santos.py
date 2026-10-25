def questao(a:int):
    print(f"""
------------------------------------------
               Questão {a}
------------------------------------------""")

questao(1)

def mensagem(funcao):
    def envelope():
        print("Iniciando execução...")
        funcao()
        print("Execução finalizada!")
    return envelope

@mensagem
def saudacao():
    print("Olá python")

saudacao()

questao(2)

def contador(funcao):
    def envelope(*args,**kwargs):
        envelope.chamadas +=1
        print(f"A funcao foi chamada {envelope.chamadas} vez(es).")
        return funcao(*args,**kwargs)
    envelope.chamadas = 0
    return envelope

@contador
def ola():
    print("Olá!")

ola()
ola()
ola()

questao(3)

def verifica_retorno(funcao):
    def envelope(*args,**kwargs):
        envelope.resultado = funcao(*args,**kwargs)
        if envelope.resultado > 0:
            print("Resultado positivo")
        elif envelope.resultado < 0:
            print("Resultado negativo")
        else:
            print("Resultado igual a zero")
        print(funcao(*args,**kwargs))
    return envelope

@verifica_retorno
def calcular(a,b):
    return a+b

calcular(10,5)
calcular(5,-10)
calcular(10,-10)

questao(4)

def requer_admin(funcao):
    def envelope(*args,**kwargs):
        usuario = args[0] if args else kwargs.get("usuario")
        if usuario and usuario.get("funcao") == "admin":
            print(f"Usuário: {usuario.get("nome")} \n Função: {usuario.get("funcao")}")
            print("Acesso autorizado")
            return funcao(*args,**kwargs)
        else:
            print(f"Usuário: {usuario.get("nome")}\nFunção: {usuario.get("funcao")}")
            print("Acesso negado")
    return envelope

usuario = {
    "nome":"Felipe",
    "funcao":"admin"
}
usuario_comum = {
    "nome":"Lucas",
    "funcao":"usuario"
}

@requer_admin
def excluir_usuario(usuario,nome):
    print(f"Usuario {nome} excluido")

excluir_usuario(usuario_comum,"João")

questao(5)

import timeit

lista = list(range(9999))

def maior_for(numeros):
    maior = numeros[0]
    for numero in numeros:
        if numero > maior:
            maior = numero
        return maior

def maior_sorted(numeros):
    return sorted(numeros)[-1]

tempo_for = timeit.timeit(lambda: maior_for(lista), number=1000)
tempo_sorted = timeit.timeit(lambda: maior_sorted(lista), number=1000)

mais_rapido = "maior_for" if tempo_for < tempo_sorted else "maior_sorted"

print(f"Maior número: {max(lista)}")
print(f"Tempo for: {tempo_for:.5f} segundos.")
print(f"Tempo sorted: {tempo_sorted:.5f} segundos.")
print(f"Mais rápido: {mais_rapido}")


        