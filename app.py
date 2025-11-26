import flask as fk
from secrets import token_hex

srv = fk.Flask(__name__)
srv.secret_key = token_hex()

@srv.get('/')
def get_home():
    return fk.render_template('home_page.html', rota_atual='/')

@srv.get('/login')
def get_login():
    return fk.render_template('login.html', rota_atual='/login')

@srv.get('/chamar_guincho')
def get_chamar_guinho():
    return fk.render_template('chamar_guincho.html', rota_atual='/chamar_guincho')

@srv.get('/historico')
def get_historico():
    return fk.render_template('historico.html', rota_atual="/historico")

@srv.post('/login')
def valida_login():
    login = fk.request.form['login']
    senha = fk.request.form['senha']
    if login == 'gabriel' and senha=='123':
        fk.session['login'] = login
        return fk.redirect('/')
    else:
        return fk.redirect('login')
    

@srv.get('/sair')
def get_sair():
    del fk.session['login']
    return fk.redirect('/')

if __name__ == '__main__':
    srv.run(host='localhost',port=5050,debug=True)