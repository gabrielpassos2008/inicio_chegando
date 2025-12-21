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

@srv.get('/cadastrar_usuario')
def get_cadastrar_usuario():
    return fk.render_template('cadastrar_usuario.html', rota_atual='/login')

@srv.get('/chamar_guincho')
def get_chamar_guinho():
    return fk.render_template('chamar_guincho.html', rota_atual='/chamar_guincho')

@srv.get('/historico')
def get_historico():
    valor = model.solicitacoes_anteriores(fk.session['id'])
    return fk.render_template('historico.html', informacao = valor , rota_atual="/historico")

@srv.get('/detalhes/<id>')
def get_detalhes_id(id):
    valor = model.solicitacoes_anteriores_datalhadas(id)
    return fk.render_template('historico_detalhado.html', informacao = valor, rota_atual = "/historico")
@srv.get('/perfil')
def get_perfil():
    valor = model.dados_perfil(fk.session['email'])
    return fk.render_template('perfil.html', informacao = valor ,rota_atual="/perfil")

@srv.post('/chamar_guincho')
def post_chamar_guincho():
    placa = fk.request.form['placa']
    endereco_origem = fk.request.form['endereco_origem']
    endereco_final = fk.request.form['endereco_final']
    id_usuarios = fk.session['id']
    if not model.cadastrar_pedido_guincho(placa,endereco_origem,endereco_final,id_usuarios):
        return fk.redirect('/')
    else:
        return fk.redirect('/chamar_guincho')

@srv.post('/cadastrar_usuario')
def post_cadastrar_usuario():
    nome = fk.request.form['nome']
    email = fk.request.form['email']
    senha = fk.request.form['senha']
    telefone = fk.request.form['telefone']
    data_nascimento = fk.request.form['data_nascimento']
    if not model.verificar_email(email):
        model.cadastrar_usuario(nome,email,senha,telefone,data_nascimento)
        return fk.redirect("/login")
    else:
        fk.flash("Este e-mail já está cadastrado. Tente outro.")
        return fk.redirect('/cadastrar_usuario')

@srv.post('/login')
def valida_login():
    email = fk.request.form['email']
    senha = fk.request.form['senha']
    id =  model.pesquisar_login(email,senha)
    if id:
        fk.session['email'] = email
        fk.session['id'] = id
        return fk.redirect('/')
    else:
        fk.flash("E-mail ou senha incorretos. Verifique os dados e tente novamente.")
        return fk.redirect('login')
    
@srv.get('/sair')
def get_sair():
    try:
        del fk.session['id']
        del fk.session['email']
        return fk.redirect('/')
    except KeyError:
        return fk.redirect('/')

if __name__ == '__main__':
    srv.run(host='localhost',port=5050,debug=True)