import mysql.connector
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
    f'Usuario: {usuario} & Senha: {senha}'
    return login(usuario, senha)

@app.route("/sos")
@app.route("/sos.html")
def sos():
    return f'Página O VÉIO CAIU'


if __name__ == "__main__":
    app.run(debug=True)


def login(usuario, senha):

    # Connect to server
    cnx = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="Jl04081998",
        database="dbteste")

    # Get a cursor
    cur = cnx.cursor()

    # Execute a query
    cur.execute("SELECT * FROM usuario WHERE nome = %s and senha = %s", (usuario, senha))

    myresult = cur.fetchone()


    # Close connection
    cnx.close()

    return myresult

#result = login('Diego', '123456')
#print(result) 