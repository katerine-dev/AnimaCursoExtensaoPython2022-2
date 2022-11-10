# Criação de funções:

preco = 1999.90

# calcular 5% de imposto, guardar na váriavel imposto e
# exibir na tela

imposto = preco * 0.05
print(imposto)

#preço com desconto
#preco_desconto = preco - (preco * 0.05)
#print(preco_desconto)

preco_2 = 100
imposto_2 = preco_2 * 0.05
print(imposto_2)

# criar uma função calcular_imposto() que calcular um
# imposto de 5% e retorna a quem pediu
# Isso é a declaração/definição da função  (como ela funciona)
def calcular_imposto(preco_produto): # preco_produto é um parâmetro ou argumento da funcão
    imposto = preco_produto * 0.05
    return imposto

# Aqui é o uso ... aqui é imposto a calcular

#preco_novo = 100
#imposto = calcular_imposto(preco_novo)
#preco_com_imposto = preco_novo + preco_com_imposto
#print(preco_com_imposto)

preco = 299
imposto = calcular_imposto(preco)
print(imposto)


