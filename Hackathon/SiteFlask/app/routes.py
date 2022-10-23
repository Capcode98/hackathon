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
    login(usuario, senha)


if __name__ == "__main__":
    app.run(debug=True)


def login(usuario, senha):
    # Connect to server
    cnx = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="123456",
        database="dbteste")

    # Get a cursor
    cur = cnx.cursor()

    # Execute a query
    cur.execute("SELECT * FROM usuario WHERE nome = %s and senha = %s", (usuario, senha))

    myresult = cur.fetchone()


    # Close connection
    cnx.close()

    return myresult

result = login('Diego', '123456')

print(result)
