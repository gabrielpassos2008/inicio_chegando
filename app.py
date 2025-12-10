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
    return fk.render_template('criar_conta.html', rota_atual='/login')

@srv.get('/chamar_guincho')
def get_chamar_guinho():
    return fk.render_template('chamar_guincho.html', rota_atual='/chamar_guincho')

@srv.get('/historico')
def get_historico():
    return fk.render_template('historico.html', rota_atual="/historico")

@srv.get('/perfil')
def get_perfil():
    valor = model.dados_perfil(fk.session['email'])
    return fk.render_template('perfil.html', informacao = valor ,rota_atual="/perfil")

@srv.post('/criar_conta')
def post_criar_conta():
    nome = fk.request.form['nome']
    email = fk.request.form['email']
    senha = fk.request.form['senha']
    telefone = fk.request.form['telefone']
    data_nascimento = fk.request.form['data_nascimento']
    model.cadastrar_usuario(nome,email,senha,telefone,data_nascimento)
    return fk.redirect("/login")

# @srv.post('/perfil')
# def post_perfil():
#         valor = model.dados_perfil(fk.session['email'])        
#         return valor

@srv.post('/login')
def valida_login():
    email = fk.request.form['email']
    senha = fk.request.form['senha']
    valor =  model.pesquisar_login(email,senha)
    if valor:
        fk.session['email'] = email
        return fk.redirect('/')
    else:
        return fk.redirect('login')
    
@srv.get('/sair')
def get_sair():
    try:
        del fk.session['email']
        return fk.redirect('/')
    except KeyError:
        return fk.redirect('/')

if __name__ == '__main__':
    srv.run(host='localhost',port=5050,debug=True)