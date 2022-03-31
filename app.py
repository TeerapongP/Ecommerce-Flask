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
  cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
  cursor.execute('SELECT * FROM product_index ORDER BY product_id LIMIT 6')
  data = cursor.fetchall()
  return render_template('index.html',data = data)

@app.route("/signout")
def signout():
  session.pop('username',None)
  return redirect('signin')

@app.route("/manga_best_seller")
def manga_best_seller():
  cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
  cursor.execute('SELECT * FROM product_bestseller ORDER BY product_id')
  data = cursor.fetchall()
  return render_template('manga_best_seller.html',data = data)

@app.route("/manga_new")
def manga_new():
  return render_template('manga_new.html')

@app.route("/manga_promotions")
def manga_promotions():
  cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
  cursor.execute('SELECT * FROM product_promotions ORDER BY product_id')
  data = cursor.fetchall()
  return render_template('manga_promotions.html',data = data)

@app.route("/promotions")
def promotions():
  return render_template('promotions.html')

@app.route("/manga_introduce")
def manga_introduce():
  return render_template('manga_introduce.html')

@app.route("/signin")
def signin():
  return render_template('signin.html')

@app.route("/submit", methods=['POST'])
def submit():
  cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
  if request.method == 'POST' and 'inputEmail' in request.form and 'inputPassword' in request.form:
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
 
    cursor.execute('SELECT * FROM user_signin_signup WHERE email = %s', (_email,))
    account = cursor.fetchone()

    if account:
      password_rs = account['pwd']
      if check_password_hash(password_rs, _password):
        session['loggedin'] = True
        session['id'] = account['id']
        session['username'] = account['username']
        session.modified = True
        print(session)
        return redirect(url_for('index',session = session))
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
      return redirect(url_for('signin'))
  elif request.method == 'POST':
      msg = 'Please fill out the form !'

  return render_template('signup.html')

if __name__ == "__main__":
  app.run(debug=True)