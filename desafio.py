# Importar a função do 'aulas-praticas-4-exemplo-conectar'

import aulas_praticas_4_exemplo_conectar as bd

conexao, cursor = bd.conectar()

# Consulta aqui a tabela grupos e exibe na tela, pedindo para o usuário digitar o grupo_id

# 1o passo: Consultar a tabela grupos

sql = "SELECT grupo_id, nome FROM grupos" # confirmando quais são os grupos que estão disponíveis
cursor.execute(sql)

grupos = cursor.fetchall() # guardar todos -  pega a consulta inteira
for grupo_id in grupos:
    print(grupo_id)

# 2o passo: Consultar a tabela pessoas_grupo

sql = "SELECT pessoa_id, grupo_id FROM pessoas_grupos" # confirmando quais são os grupos que estão disponíveis
cursor.execute(sql)

pessoas_grupos = cursor.fetchall() # guardar todos -  pega a consulta inteira
for grupo_id in pessoas_grupos:
    print(grupo_id)

# Pedir para que o usuário informe o grupo:
pessoa_id = 12
grupo_id = input("\nInforme o grupo do super herói: \n(1) Sociedade da Justiça da América; \n(2) Liga da Justiça; \n(3) Tropa dos Lanternas Verdes; \n(4) Esquadrão Suicida \nResposta:")

sql = f"INSERT or REPLACE INTO pessoas_grupos (pessoa_id,  grupo_id) VALUES ('{pessoa_id}', '{grupo_id}')"

cursor.execute(sql)

# Confirmar o INSERT com commit() e fechar o banco

conexao.commit()
conexao.close()

# visualizar
for grupo_id in pessoas_grupos:
    print(grupo_id)

