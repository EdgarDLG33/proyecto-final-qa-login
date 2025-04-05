
from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
from werkzeug.security import check_password_hash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'secret_key'

def get_db_connection():
    conn = sqlite3.connect('usuarios.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM usuario WHERE username = ?', (username,)).fetchone()
        if user and check_password_hash(user['password_hash'], password):
            session['user_id'] = user['id']
            session['username'] = user['username']
            conn.execute('INSERT INTO sesion (usuario_id, fecha_inicio) VALUES (?, ?)',
                         (user['id'], datetime.now().isoformat()))
            conn.commit()
            conn.close()
            return redirect(url_for('dashboard'))
        flash('Credenciales inválidas.')
        conn.close()
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', username=session['username'])

@app.route('/logout')
def logout():
    user_id = session.get('user_id')
    if user_id:
        conn = get_db_connection()
        conn.execute('UPDATE sesion SET fecha_cierre = ? WHERE usuario_id = ? AND fecha_cierre IS NULL',
                     (datetime.now().isoformat(), user_id))
        conn.commit()
        conn.close()
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
