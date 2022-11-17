# Inserindo dados no banco
# comandos idênticos ao aulas-praticas-4-banco-dados
import sqlite3

conexao = sqlite3.connect("data/dc_universe.db") # 1o. parâmetro é o nome do arquivo

cursor = conexao.cursor()

# 4o. passo: comando para inserir um herói/vilão

sql = "INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES (12, 'The Flash', 'Barry Allen', 'Herói(na)')"

# 5o. passo: Executar o camando SQL
#cursor.execute(sql)

print(cursor.execute(sql))

# 6o. passo: Confirmar o INSERT com commit() e fechar o banco

conexao.commit()
conexao.close()