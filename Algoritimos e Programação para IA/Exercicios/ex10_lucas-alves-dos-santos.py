def questao(a:int):
    print(f"""
-----------------------------------------
            Questão {a}
-----------------------------------------""")

questao(1)

def numero(n):
    if n > 0:
        print("Número positivo")
    elif n < 0:
        print("Número negativo")
    else:
        print("O número é zero")

n = int(input("Digite um número: "))
numero(n)

questao(2)

def validador(mensagem):
    while True:
        try:
            num = int(input(mensagem))
            if num < 0:
                print("Número menor que zero. Tente novamente. \n")
                continue
            return num
        except ValueError:
            print("O número digitado precisa ser um algarismo númerico inteiro. \n")

def calc_basic():
        a = validador("Digite um número inteiro positivo: ")
        b = validador("Digite um número inteiro positivo: ")
        while True:
            operacao = input("Digite uma operação: \n+\n-\n*\n/\n")
            try:
                match operacao:
                    case "+": print(f"N1: {a}\nN2: {b}\nOperação: +\nResultado: {a+b}")
                    case "-": print(f"N1: {a}\nN2: {b}\nOperação: -\nResultado: {a-b}")
                    case "*": print(f"N1: {a}\nN2: {b}\nOperação: *\nResultado: {a*b}")
                    case "/": print(f"N1: {a}\nN2: {b}\nOperação: /\nResultado: {a/b}")
                    case _: 
                        print("Operação invalida tente novamente.\n")
                        continue
                break
            except ZeroDivisionError:
                print("\n Impossivel dividir por zero!")
                if b == 0:
                    b = validador("Digite novamente o segundo número: ")

calc_basic()

questao(3)

def eh_bissexto(number: int):
    if number < 0:
        return False

    elif (number % 4 == 0 and number % 100 != 0) or number % 400 == 0:
        return True

    else:
        return False

print(eh_bissexto(2028))

questao(4)

def login(funcao):
    def envelope(*args, **kwargs):
        dados = args[0] if args else kwargs.get("usuario")
        if (dados and dados.get("usuario") == "admin") and (dados and dados.get("senha") == "1234"):
            print("Login realizado com sucesso")
            return funcao(*args, **kwargs)
        else:
            print("Usuário ou senha incorretos")
    return envelope

usuario = {
    "usuario":"admin",
    "senha":"1234"
}

usuario_invalido = {
    "usuario": "Lucas",
    "senha": "123"
}

@login
def validador(usuario):
    print(f"Bem vindo {usuario.get("usuario")}")

validador(usuario_invalido)

questao(5)

def quebra_cpf(cpf: str):
    digitos, separador, digito_verificador = cpf.partition("-")
    cpf_separado = [digitos,digito_verificador]
    return cpf_separado

def limpa_cpf(cpf):
    cpf_limpo = cpf[0].replace(".","")
    return cpf_limpo
    

def valida_dv(cpf,dv):
    pesos = [10,9,8,7,6,5,4,3,2]
    resultado = sum(int(d) *p for d,p in zip(cpf,pesos))
    resto = resultado % 11
    subtracao = 11 - resto

    if subtracao >= 10:
        subtracao = 0

    cpf1 = f"{cpf}{subtracao}"

    cpf1 = cpf1[1:]
    resultado2 = sum(int(d) *p for d,p in zip(cpf1,pesos))
    resto2 = resultado2 % 11
    subtracao2 = 11 - resto2
    if subtracao2 >= 10:
            subtracao2 = 0

    resultado_cpf = f"{cpf}{subtracao}{subtracao2}"
    cpf_entrada = f"{cpf}{dv}"

    if resultado_cpf == cpf_entrada:
         return True
    else:
         return False

def valida_cpf(cpf):
    print(f"CPF do usuário é: {cpf}")
    print(f"O DV é: {quebra_cpf(cpf)[1]}")
    cpf_valido = valida_dv(limpa_cpf(quebra_cpf(cpf)),quebra_cpf(cpf)[1])
    if cpf_valido == True: 
        print("CPF válido")
    else:
         print("CPF inválido")

valida_cpf("518.313.810-95")

questao(6)

def dia_semana():
     while True:
        try:
            a = int(input("Digite um número de 1 a 7 correspondente ao dia da semana: "))
        except:
             print("Digite um algarismo numérico")

        match a:
             case 1: print("Domingo")
             case 2: print("Segunda-feira")
             case 3: print("Terça-feira")
             case 4: print("Quarta-feira")
             case 5: print("Quinta-feira")
             case 6: print("Sexta-feira")
             case 7: print("Sábado")
             case _: 
                print("Dia inválido.")
                continue
        break

dia_semana()
    

    



