import flask as fk
from secrets import token_hex
import model

srv = fk.Flask(__name__)
srv.secret_key = token_hex()

@srv.get('/')
def get_home():
    return fk.render_template('home_page.html', rota_atual='/')

@srv.get('/login')
def get_login():
    return fk.render_template('login.html', rota_atual='/login')

@srv.get('/criar_conta')
def get_criar_conta():
    nome = fk.request.form['nome']
    email = fk.request.form['email']
    senha = fk.request.form['senha']
    model.cadastrar_usuario(nome,email,senha)
    return fk.render_template('criar_conta.html', rota_atual='/login')

@srv.get('/chamar_guincho')
def get_chamar_guinho():
    return fk.render_template('chamar_guincho.html', rota_atual='/chamar_guincho')

@srv.get('/historico')
def get_historico():
    return fk.render_template('historico.html', rota_atual="/historico")

@srv.get('/perfil')
def get_perfil():
    return fk.render_template('perfil.html', rota_atual="/perfil")


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
    try:
        del fk.session['login']
        return fk.redirect('/')
    except KeyError:
        return fk.redirect('/')

if __name__ == '__main__':
    srv.run(host='localhost',port=5050,debug=True)