import MySQLdb
from django.shortcuts import redirect
from flask import Flask, flash, render_template, request, redirect, url_for , session
from flask_mysqldb import MySQL
import re
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os

#Yume Nishimiya
app = Flask(__name__)

app.secret_key = "secret key"
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

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


# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/product/add', methods=['POST'])
# def addproduct():
#     _id = request.form['inputID']
#     _name = request.form['inputName']
#     _price = request.form['inputPrice']

#     if 'file' in request.files:
#         file = request.files['file']
#         # if file : ไฟล์ค่าไม่เป็น None
#         # not(file.filename == '') : user ต้องอัพโฟลไฟล์
#         # allowed_file(file.filename) : นามสกุลไฟล์ต้องเป็น 'png', 'jpg', 'jpeg', 'gif'
#         if file and not(file.filename == '') and allowed_file(file.filename):
#             # หาชื่อไฟล์
#             filename = secure_filename(file.filename)
#             # หานามสกุลไฟล์
#             extension = os.path.splitext(filename)[1]
#             # ตั้งชื่อ ไฟล์ไปที่โฟลเดอร์ static/images/products ชื่อเปลี่ยน รหัสสินค้า.นามสกุลตามที่upload
#             upload_filename = os.path.join(
#                 './static/images/index/', _id + extension)
#             # บันทึกไฟล์ลงไปบน server
#             file.save(upload_filename)
#             # ชื่อไฟล์ที่จะใส่ลงฐานข้อมูล
#             _file = _id + extension

#     # เชคว่า ค่า id, name และ price ไมเป็นค่าว่าง
#     if _name and _price and request.method == 'POST':
#         try:
#             cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#             # ? คือให้เติมด้วย data
#             cursor.execute(''' INSERT INTO product_index VALUES(NULL,%s,%s,%s)''',(_name,_price,_file))
#             mysql.connection.commit()
#         except Exception as e:
#             print(e)
#         finally:
#             cursor.close()
#     return 'success'

# @app.route("/")
# def product():
#   return render_template('insert_product.html')

if __name__ == "__main__":
  app.run(debug=True)