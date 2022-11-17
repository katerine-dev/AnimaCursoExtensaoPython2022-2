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

# A função pode terminar em uma condição também (if)

# Aqui é o uso ... aqui é imposto a calcular

#preco_novo = 100
#imposto = calcular_imposto(preco_novo)
#preco_com_imposto = preco_novo + preco_com_imposto
#print(preco_com_imposto)

preco = 299
imposto = calcular_imposto(preco)
print(imposto)

# Explicação de variável logal x global
#print(preco)
#preco_produto = 100
#print(preco_produto) #????


# agora calcular imposto a alíquota é 7%:

valores = [1.99, 24.50, 78.29, 1515.5]

def calcular_imposto(preco_produto):
    imposto = preco_produto * 0.07
    return imposto
# se eu quiser calcular o imposto destes quatro
# valores e exibir na tela assim: "O imposto de....
# é ..."
for valor in valores:
    imposto = calcular_imposto(valor)
    print(f"O imposto de {valor} é {imposto}")

# Declarar um função calcular_imposto_aliquota que recebe dois parâmetros:
# o preço do produto e a alíquota de imposto a ser aplicada e retorna o imposto calculado.
# Se a aliquota não for informada, utilize 7% como padrão.

def calcular_imposto_aliquota(valor, aliquota = 7): # valor default
    imposto = valor * (aliquota / 100)
    return imposto

# Resposta com default:
for valor in valores:
    imposto = calcular_imposto_aliquota(valor)
    print(f"O imposto de {valor} é {imposto}")

# Resposta: E se agora o imposto for 10%:
for valor in valores:
    imposto = calcular_imposto_aliquota(valor, 10)
    print(f"O imposto de {valor} é {imposto}")