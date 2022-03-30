
import MySQLdb
from django.shortcuts import redirect
from flask import Flask, flash, render_template, request, redirect, url_for , session
from flask_mysqldb import MySQL
import re
from werkzeug.security import generate_password_hash, check_password_hash

#Yume Nishimiya
app = Flask(__name__)

app.secret_key = "secret key"
# Intialize MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345678'
app.config['MYSQL_DB'] = 'bookstore'

mysql = MySQL(app)

@app.route("/index")
def index():
  if 'loggedin' in session:
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM user_signin_signup WHERE username = %s', (session['username'],))
    account = cursor.fetchone()
    return render_template('index.html', account=account)
  return redirect(url_for('index'))  

@app.route("/signout", methods=['POST'])
def signout():
  session.pop('username',None)
  return render_template('index.html')

@app.route("/manga_best_seller")
def manga_best_seller():
  return render_template('manga_best_seller.html')

@app.route("/signin")
def signin():
  return render_template('signin.html')

@app.route("/submit", methods=['POST'])
def submit():
  cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
  if request.method == 'POST' and 'inputUsername' in request.form and 'inputPassword' in request.form:
    _username = request.form['inputUsername']
    _password = request.form['inputPassword']

    cursor.execute('SELECT * FROM user_signin_signup WHERE username = %s', (_username,))
    account = cursor.fetchone()

    if account:
      password_rs = account['pwd']
      if check_password_hash(password_rs, _password):
        session['loggedin'] = True
        session['id'] = account['id']
        session['username'] = account['username']
        return redirect(url_for('index'))
      else:
        flash('Incorrect username/password')
    else:
      flash('Incorrect username/password')

@app.route("/signup", methods=['GET','POST'])
def signup():
  cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

  if request.method == 'POST' and 'inputEmail'in request.form and 'inputUsername' in request.form and 'inputPassword' in request.form:
    
    email_ = request.form['inputEmail']
    username = request.form['inputUsername']
    password = request.form['inputPassword']
    
    _hashed_password = generate_password_hash(password)

    cursor.execute(''' SELECT * FROM user_signin_signup WHERE username = (%s)''',(username,))
    account = cursor.fetchone()
    print(account)

    if account:
      msg = 'Account already exists !'
    elif not re.match(r'[^@]+@[^@]+\.[^@]+', email_):
      msg = 'Invalid email address !'
    elif not re.match(r'[A-Za-z0-9]+', username):
      msg = 'Username must contain only characters and numbers !'
    elif not username or not password or not email_:
      msg = 'Please fill out the form !'
    else:
      cursor.execute(''' INSERT INTO user_signin_signup VALUES(NULL,%s,%s,%s)''',(email_,username,_hashed_password))
      mysql.connection.commit()
      msg = 'You have successfully registered !'
      return redirect(url_for('index'))
  elif request.method == 'POST':
      msg = 'Please fill out the form !'

  return render_template('signup.html')

if __name__ == "__main__":
  app.run(debug=True)