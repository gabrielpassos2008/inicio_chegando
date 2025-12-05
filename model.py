import sqlite3

def cadastrar_usuario(nome,email,senha):
    with sqlite3.connect('banco_chegando_pi.db') as conn:
        sql_cadastrar_usuario = ('''
        INSERT INTO usuarios (nome,email,senha)
        VALUES(?,?,?)
        ''')
        conn.execute(sql_cadastrar_usuario,(nome,email,senha))

def pesquisar_login(email,senha):
    with sqlite3.connect('banco_chegando_pi.db') as conn:
        cursor = conn.cursor()
        sql_pesquisar_login = ('''
        SELECT email,senha
        FROM usuarios
        WHERE email = ? AND senha = ?
        ''') 
        resultado = cursor.execute(sql_pesquisar_login,(email,senha))
        resultado = cursor.fetchone()
        if resultado:
            return True
        else:
            return False