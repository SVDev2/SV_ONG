#app.py não funcional ainda deve-se especificar as rotas das páginas HTML


from flask import Flask, render_template

app = Flask(__name__)

#app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

#@app.after_request
#def add_header(response):
#    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
#    response.headers["Pragma"] = "no-cache"
#    response.headers["Expires"] = "0"
#    return response

@app.route("/")
def inicio():
    return render_template("pages/home.html")
    
@app.route("/sobre")
def sobre():
    return render_template("pages/sobre.html")
    
@app.route("/entrar")
def entrar():
    return render_template("auth/entrar.html")
    
@app.route("/cadastrar")
def cadastrar():
    return render_template("auth/cadastrar.html")
    
@app.route("/termos")
def termos():
    return render_template("pages/termos.html")
    
@app.route("/doacao")
def doacao():
    return render_template("pages/doacao.html")
    
@app.route("/configuracoes")
def configuracoes():
    return render_template("settings/configuracoes.html")
    
@app.route("/banner")
def banner():
    return render_template("footer/banner_cookies.html")
    
@app.route("/redefinir-senha")
def recuparaS():
    return render_template("auth/recupera_senha.html")
    
@app.route("/slide")
def slide():
    return render_template("footer/slide.html")
    
@app.route("/desenvolvimento")
def desenvolvimento():
    return render_template("includes/msg_desenvolvimento")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=4000)