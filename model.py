import sqlite3
def verificar_email(email):
    with sqlite3.connect('banco_chegando_pi.db') as conn:
        cursor = conn.cursor()
        sql_verificar_email = ('''
        SELECT email
        FROM usuarios
        WHERE email = ?
        ''')
        cursor.execute(sql_verificar_email,(email,))
        resultado = cursor.fetchone()
        if resultado:
            return True
        else:
            return False
        
def cadastrar_usuario(nome,email,senha,data_nascimento,telefone):
    if not verificar_email(email):
        with sqlite3.connect('banco_chegando_pi.db') as conn:
            sql_cadastrar_usuario = ('''
            INSERT INTO usuarios (nome,email,senha,data_nascimento,telefone)
            VALUES(?,?,?,?,?)
            ''')
            conn.execute(sql_cadastrar_usuario,(nome,email,senha,data_nascimento,telefone))
            return False
    else:
        return True
    
def pesquisar_login(email,senha):
    with sqlite3.connect('banco_chegando_pi.db') as conn:
        cursor = conn.cursor()
        sql_pesquisar_login = ('''
        SELECT email,senha
        FROM usuarios
        WHERE email = ? AND senha = ?
        ''') 
        cursor.execute(sql_pesquisar_login,(email,senha))
        resultado = cursor.fetchone()
        if resultado:
            return True
        else:
            return False
        
def dados_perfil(email):
    with sqlite3.connect('banco_chegando_pi.db') as conn:
        cursor = conn.cursor()
        sql_dados_perfil = ('''
        SELECT nome,email,data_nascimento,telefone
        FROM usuarios
        where email = ?
        ''')
        cursor.execute(sql_dados_perfil,(email,))
        resultado = cursor.fetchall()
        return resultado 


        
