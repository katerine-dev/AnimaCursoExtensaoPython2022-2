# Importar a função do 'aulas-praticas-4-exemplo-conectar'

import aulas_praticas_4_exemplo_conectar as bd

conexao, cursor = bd.conectar()

nome = input("Informe o nome do herói/vilão: ")
nome_civil = input("Informe o nome civil do herói/vilão (sua identidade secreta): ")
tipo_numerico = input("Tecle 1 para Herói(na) ou 2 para Vilã(o): ")

# Consulta para o valor máximo usado no banco

sql = "SELECT MAX(pessoa_id)+1 FROM pessoas" # vai pegar o 12 - "incrementar" - vai pegar a ultima linha e me retornar a próxima
cursor.execute(sql)
pessoa_id = cursor.fetchone()[0] #só a primeira coluna

if tipo_numerico == "1":
    tipo = "Herói(na)"
else:
    tipo = "Vilã(o)"

sql = f"INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES ({pessoa_id}, '{nome}', '{nome_civil}', '{tipo}')"

cursor.execute(sql)

# Insert pessoas_grupos
# INSERT INTO pessoas_grupos (pessoa_id, grupo_id) VALUES (x, y) "5,2"

conexao.commit()
conexao.close()



