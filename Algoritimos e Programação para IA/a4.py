## Estruturas de decisão

if True:
    print("Olá")

idade = 20
if idade > 21:
    print("maior")
else:
    print("Menor")

if idade < 5:
    print("Primeira infância")
elif idade < 10:
    print("Segunda infância")
elif idade < 18:
    print("Adolescencia")
else:
    print("Adulto")

clientes = []
cliente = {
    "nome":"Lucas",
    "idade":27,
    "id":0
}
clientes.append(cliente)
print(clientes)

i = 0
while i < 10:
    i += 1
    print(i)

for i in range(10):
    print(i)
