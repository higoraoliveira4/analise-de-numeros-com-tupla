cont = 0
num1 = (int(input('Digite um numero: ')))
num2 = (int(input('Digite outro numero: ')))
num3 = (int(input('Digite mais um numero: ')))
num4 = (int(input('Digite o ultimo numero: ')))

numeros = (num1, num2, num3, num4)

print (f"O número 9 apareceu {numeros.count(9)} vezes na lista.")
if 3 in numeros:
    print (f"O número 3 apareceu na posição {numeros.index(3)+1}")
else:
    print ("O valor 3 não foi encontrado em nenhuma posição")
for n in numeros:
    if n % 2 == 0:
        cont += 1
print (f"{cont} valores são número par.")