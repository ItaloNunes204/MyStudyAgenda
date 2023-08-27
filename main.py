from flask import Flask, render_template, redirect, request, session, flash
from flask_session import Session
import formatador as fr
import classes
import banco as bd


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['SECRET_KEY'] = "teste_palavra_chave"
Session(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/cadastro_conta", methods=["POST", "GET"])
def cadastro_conta():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        senha = request.form.get("senha")
        conf_senha = request.form.get("confsenha")
        curso = request.form.get("curso")
        periodo = request.form.get("periodo")
        universidade = request.form.get("universidade")
        if senha != conf_senha:
            flash("As senhas não conferem")
            return redirect("/cadastro_conta")
        else:
            senha = fr.codificando(senha)
            conta = classes.Conta(nome, senha, curso, periodo, universidade, True, True, 0, email)
            if bd.cria_conta(conta):
                session["name"] = email
                return redirect('/cliente')
            else:
                flash("Erro ao cadastrar a conta")
    else:
        return render_template("cadastroConta.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")
        if bd.login(email, senha):
            session["name"] = email
            return redirect('/cliente')
        else:
            flash("Conta invalida")
    else:
        render_template("login.html")


@app.route('/cliente')
def cliente():
    if not session.get("name"):
        return redirect("/login")
    else:
        return render_template("inicio.html")


if __name__ == "__main__":
    app.run(debug=True)
