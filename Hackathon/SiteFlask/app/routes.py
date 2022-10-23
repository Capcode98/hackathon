from app import app
from flask import render_template, request

@app.route('/')
@app.route('/index')
@app.route('/emergencia')
@app.route('/emergencia.html')
def index():
    return render_template("emergencia.html")

@app.route("/login")
@app.route("/login.html")
def login():
    return render_template("login.html")

@app.route("/<string:nome>")
def error(nome):
    return f'Página ({nome}) não existe'

@app.route("/autenticar", methods=['POST'])
def autenticar():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')
    return f'usuario: {usuario} e senha: {senha}'


if __name__ == "__main__":
    app.run(debug=True)