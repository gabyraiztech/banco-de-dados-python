import sqlite3

#1- conectando noBD
conexao = sqlite3.connect('titulo.bd')
cursor = conexao.cursor()

# 2 - Exclusao de dados
id = (1, 2)
cursor.execute(
    """
        DELETE FROM filmes
        WHERE ID in (?, ?)
    """,
    id
)

conexao.commit()

print("Dados excluidos com sucesso")