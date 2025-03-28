from flask import Flask, render_template, redirect, request, url_for, flash
import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = 'BIEL'

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Diamante1608',
    'database': 'clientes'
}

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    nome = request.form.get('nome')
    senha = request.form.get('senha')

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM clientes WHERE nome = %s AND senha = %s", (nome, senha))
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if user:
        return redirect(url_for('dashboard'))
    
    flash("Usuário ou senha inválidos", "error")
    return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    return "<h1>Bem-vindo ao painel de controle!</h1>"

@app.route('/create-user', methods=['GET', 'POST']) # Alteração aqui!
def create_user():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        telefone = request.form.get('telefone')
        genero = request.form.get('genero')
        data_nascimento = request.form.get('data_nascimento')
        cidade = request.form.get('cidade')
        estado = request.form.get('estado')
        endereco = request.form.get('endereco')
        senha = request.form.get('senha')

        if not nome or not email or not senha:
            flash("Nome, email e senha são obrigatórios!", "error")
            return redirect(url_for('create_user'))

        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT INTO clientes (nome, email, telefone, genero, data_nascimento, cidade, estado, endereco, senha) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (nome, email, telefone, genero, data_nascimento, cidade, estado, endereco, senha))
            conn.commit()
            flash("Usuário cadastrado com sucesso!", "success")
            return redirect(url_for('home'))
        except mysql.connector.IntegrityError:
            flash("Erro: Email já cadastrado!", "error")
        finally:
            cursor.close()
            conn.close()

    return render_template('create_user.html')

if __name__ == "__main__":
    app.run(debug=True)