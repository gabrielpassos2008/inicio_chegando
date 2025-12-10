import sqlite3

def cadastrar_usuario(nome,login,senha,data_nascimento,telefone):
    with sqlite3.connect('banco_chegando_pi.db') as conn:
        sql_cadastrar_usuario = ('''
        INSERT INTO usuarios (nome,email,senha,data_nascimento,telefone)
        VALUES(?,?,?,?,?)
        ''')
        conn.execute(sql_cadastrar_usuario,(nome,login,senha,data_nascimento,telefone))
def pesquisar_login(login,senha):
    with sqlite3.connect('banco_chegando_pi.db') as conn:
        cursor = conn.cursor()
        sql_pesquisar_login = ('''
        SELECT email,senha
        FROM usuarios
        WHERE email = ? AND senha = ?
        ''') 
        valor = cursor.execute(sql_pesquisar_login,(login,senha))
        valor = cursor.fetchone()
        if valor:
            return True
        else:
            return False
        
def dados_perfil(login):
    with sqlite3.connect('banco_chegando_pi.db') as conn:
        cursor = conn.cursor()
        sql_dados_perfil = ('''
        SELECT nome,email,data_nascimento,telefone
        FROM usuarios
        where email = ?
        ''')
        valor = cursor.execute(sql_dados_perfil,(login,))
        valor = cursor.fetchall()
        return valor 


