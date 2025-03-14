# O laço de repetição "for" (loop for)

sequencia = ["Ana", "Abigail", "Inês", "Isa"]

for elemento in sequencia:
    print(elemento)

numeros = [2, 7, 1, 9, 15]
numeros.sort()
for numero in numeros:
    print(numero, end=" ")
print()

tupla = ("Palmeiras", "Corinthians", "São Paulo", "Santos" )
for time in tupla:
    print(time, end=" ")
print()

dicionário = {'SP':"São Paulo", 'RJ':"Rio de Janeiro", "MG":"Minas"}
for estado in dicionário:
    print(estado)

print()
# Função Range
# Range(inicio, fim, passo)
pontos = range(3, 9, 2)
for ponto in pontos:
    print(pontos)

print()
for valor in range(20):
    print(valor)

lista_numerica = list(range(1, 51))
for n in lista_numerica:
    print(n)

print(lista_numerica)

# Função Enumerate()
paises = ["Brasil", "França", "Russia", "Alemanha", "Espanha", "Itália"]
for indice in paises:
    print(f"\Índice: {indice}: Valor: {valor}")


for i, v in enumerate(dicionário):
    print(f"{i} - {v}")
