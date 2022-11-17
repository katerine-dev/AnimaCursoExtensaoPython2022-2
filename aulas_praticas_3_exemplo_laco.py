# EXEMPLO LAÇO

contador = 1

# Exibir de 1 até 10 repetidamente:
while(contador <= 10):
    print(contador)
    contador = contador + 1 # contador += 1

fruta = "Morango"

# Lista
lista_frutas = ["morango", "laranja", "perâ"]
# quero exibir apenas a 3a. fruta
print(lista_frutas[2]) # lembrar que começa com zero
print("\nExemplo de lista")
print(len(lista_frutas))
# Vetor
vetor_frutas = ("morango", "laranja", "perâ")
print("\nExemplo de vetor")
print(len(vetor_frutas)) # para comprimento do vetor - length = comprimento

# Diferença de Listas para Vetor em python:
# Um vetor, ao ser criado, já tem o tamanho pré-determinado na criação, não
# podendo mais ser alterado. Uma lista possui um tamanho dinâmico, na medida que elementos
# forem sendo incluídos ou removidos.

frutas = ["morango", "laranja", "perâ", "maça"]

frutas.append("manga") # quero incluir uma fruta nova (ao final)
print("\nExemplo das frutas com len...")
print(len(frutas))

print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[3])
print(frutas[4])
print("\nExemplo das frutas com while...")

i=0 # geralmente é i (index)
while(i<5):
    print(frutas[i])
    i = i + 1

# Laço for (python for = for each/ para cada)
print("\nExemplo das frutas com FOR...")

for fruta in frutas: # sem parênteses
    print(fruta)

for i in frutas: # sem parênteses
    print(i)
