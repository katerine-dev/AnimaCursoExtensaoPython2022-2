# Acessando banco de dados
# 1o. passo : importar a biblioteca sqlite3

import sqlite3

# 2o. passo: Vamos estabelecer uma conexão com o banco

conexao = sqlite3.connect("data/dc_universe.db") # 1o. parâmetro é o nome do arquivo

# 3o. passo: "cursor" - Criar um objeto do tipo cursor

cursor = conexao.cursor()

# 4o. passo: Comando SQL do banco
sql = "SELECT pessoa_id, nome, nome_civil, tipo FROM pessoas" #comando de consulta

# 5o. passo: Executar o comando SQL no SQLite (cursor)

cursor.execute(sql)

# 6o. passo: Exibir a consulta com todos os nomes de heróis e vilões do banco de dados

pessoas = cursor.fetchall() # guardar todos -  pega a consulta inteira
for pessoa in pessoas:
    print(pessoa)

for pessoa in pessoas:
    print(f"Nome: {pessoa[1]} ({pessoa[3]})")

