numeros = []
index = 0

while index < 5:
    num = int(input("Digite um número: "))
    numeros.append(num)
    index += 1

print(f'Os números lidos: {numeros}')

numeros.sort()

print('Em ordem fica assim:')
print(numeros)
