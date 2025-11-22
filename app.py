import flask as fk
from secrets import token_hex

srv = fk.Flask(__name__)
srv.secret_key = token_hex()

@srv.get('/')
def get_home():
    return fk.render_template('home_page.html')

@srv.get('/login')
def get_login():
    return fk.render_template('login.html')

@srv.post('/login')
def valida_login():
    login = fk.request.form['login']
    senha = fk.request.form['senha']
    if login == 'gabriel' and senha=='123':
        fk.session['login'] = login
        return fk.redirect('/')
    else:
        return fk.redirect('login')
    

if __name__ == '__main__':
    srv.run(host='localhost',port=5050,debug=True)