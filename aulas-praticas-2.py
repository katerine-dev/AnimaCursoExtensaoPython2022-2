# Aula 2: Comando input(): quero permitir que
# o usuário digite algo...

nome = input("Digite seu nome: ")

# comando de saída... exibir na tela
print(f"Boa noite, {nome}")

# Pede a idade para usuário "Qual sua idade"?
idade_usuario = int(input("Qual é a sua idade? "))

# Exiba "Sua idade é..."
#print(f"Sua idade é {idade_usuario}")

# O dobro da sua idade é:
dobro_idade = idade_usuario * 2

print("O dobro da sua idade é {}".format(dobro_idade))

# Estrutura condicional - o famoso "SE"
# Se a pessoa for maior de ideade, mostre:
# "Você é maior de idade, ótimo! Já pode beber ou dirigir!"

if idade_usuario >= 18:
    print("Você é maior de idade, ótimo! Já pode beber ou dirigir!")
else:
    print("Volte para casa!") # o else não tem obrigação

# E se eu quisesse perguntar o gênero (M = masculino; F = Feminino)
# Mostre (...e você também precisa/precisou prestar serviço
# militar obrigatório)

genero = input("Qual é o seu gênero? M = Masculino, F = Feminino, O = Outros: ")

if idade_usuario >= 18 and genero == "M":
    print("...e você também precisa/precisou prestar serviço militar obrigatório")
    #if idade_usuario == 18:
        #print("Se apresente no quartel") # condição dentro de condição.
else:
    print("Você foi liberada do serviço militar obrigatório")
if idade_usuario < 18:
        print("Você é uma criança")

# elif (else if)
