# Aula 1: Meu primeiro projeto Python!!

# print() = comando de saída
print("Hello world!")

# Variável: (string)
variavel_string_nome = "Katerine Witkoski"
variavel_inteira_idade = 29

# Exibir o meu nome (que está dentro da variável)
print(variavel_string_nome)
print(variavel_inteira_idade)

# Quando quiser exibir a frase "Minha idade é "  completando
# com o conteúdo da variável idade

print("Minha idade é "+str(variavel_inteira_idade)+" anos") # concatenação (precisa ser da mesma classe)
print(f"Minha idade é {variavel_inteira_idade}") # precisa colocar o f de formatação de valores
print("Minha idade é {}".format(variavel_inteira_idade)) # .format = formatação de valores
print("Minha idade é", variavel_inteira_idade) # funciona também (mas não é concatenação)

# Quando quiser exibir "Meu nome é ... e tenho ...
# anos ..."  trocando pelas variáveis nome e idade

print("Meu nome é {} e tenho {} anos".format(variavel_string_nome, variavel_inteira_idade))