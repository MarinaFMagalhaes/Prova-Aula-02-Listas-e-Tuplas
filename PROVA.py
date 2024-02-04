'''Faça um programa que solicite ao usuário que digite 10 valores para preencher uma lista. 
Em seguida, o programa deve separar os números pares e ímpares em listas diferentes. 
Por fim, exiba na tela os números pares, os números ímpares em uma tupla, a quantidade de números 
pares e ímpares presentes na lista, e a soma de todos os números pares e ímpares, respectivamente.'''

lista_valores = []
for x in range(10):
    valor = int(input(f"Digite o {x+1}º valor: "))
    lista_valores.append(valor)

pares = [numero for numero in lista_valores if numero % 2 == 0]
impares = [numero for numero in lista_valores if numero % 2 != 0]

print("Números pares:", pares)
print("Números ímpares:", tuple(impares))
print("Quantidade de números pares:", len(pares))
print("Quantidade de números ímpares:", len(impares))
print("Soma dos números pares:", sum(pares))
print("Soma dos números ímpares:", sum(impares))