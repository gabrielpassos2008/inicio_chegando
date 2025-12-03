import sqlite3

def cadastrar_usuario(nome,email,senha):
    with sqlite3.connect('banco_chegando_pi.db') as conn:
        sql_cadastrar_usuario = ('''
        INSERT INTO usuarios (nome,email,senha)
        VALUES(?,?,?)
        ''')
        conn.execute(sql_cadastrar_usuario,(nome,email,senha))
