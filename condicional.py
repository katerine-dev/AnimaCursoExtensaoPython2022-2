# Condição - if - else
# pede o nome do aluno e sua nota (de 0 a 10) e, se ele
# tirou nota 10, mostra "Você é bichão, mesmo..."

nome_aluno = input("Qual é o seu nome? ")
nota_aluno = float(input("Qual foi a sua nota? (de 0 a 10)"))

if nota_aluno == 10:
    print("Você é bichão, mesmo {}!".format(nome_aluno))
elif nota_aluno >= 6 and nota_aluno < 10:
    print("Você passou!") # 3 condições
else: # é sempre automaticamente o que as duas condições não tratamento
    print("Vá estudar {}!".format(nome_aluno))
