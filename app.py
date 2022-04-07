from email.policy import default
import MySQLdb
from django.shortcuts import redirect
from flask import Flask, flash, render_template, request, redirect, send_file, url_for , session
from flask_mysqldb import MySQL
import re
from werkzeug.security import generate_password_hash, check_password_hash
from itertools import chain, combinations
from mlxtend.frequent_patterns import association_rules
from mlxtend.frequent_patterns import fpgrowth
from tqdm import tqdm
import pandas as pd

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
@app.route("/")
def index():
  cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
  cursor.execute('SELECT * FROM products WHERE product_id < 7')
  data = cursor.fetchall()
  return render_template('index.html',data = data)

@app.route("/signout")
def signout():
  session.pop('username',None)
  return redirect('signin')

@app.route("/manga_best_seller")
def manga_best_seller():
  cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
  cursor.execute('SELECT * FROM products WHERE product_id > 6 AND product_id <= 18')
  data = cursor.fetchall()
  return render_template('manga_best_seller.html',data = data)


@app.route("/manga_introduce")
def manga_introduce():
  cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
  cursor.execute('SELECT * FROM products WHERE product_id > 18 AND product_id <= 30')
  data = cursor.fetchall()
  return render_template('manga_introduce.html',data=data)

@app.route("/manga_new")
def manga_new():
  cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
  cursor.execute('SELECT * FROM products WHERE product_id > 30 AND product_id <= 42')
  data = cursor.fetchall()
  return render_template('manga_new.html',data = data)

@app.route("/manga_promotions")
def manga_promotions():
  cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
  cursor.execute('SELECT * FROM products WHERE product_id > 42 AND product_id <= 46')
  data = cursor.fetchall()

  cursor_ = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
  cursor_.execute('SELECT * FROM out_of_stock')
  items_ = cursor_.fetchall()

  return render_template('manga_promotions.html',data = data, items_ = items_)


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

@app.route('/shopping_cart')
def shopping_cart():
    return render_template('shopping_cart.html')

@app.route('/clear-item')
def clear_item():
  try:
  # การทำตะกร้าให้ว่างไม่ควรใช้ session.clear() เพราะว่าถ้าเราทำระบบ user password
  # username password ใน session จะหายไปด้วย
  # ควรใช้ session.pop('product_items') เพื่อลบเฉพาะ product_items
    session.pop('product_items') # clear session
    return render_template('shopping_cart.html')
  except Exception as e:
    print(e)

@app.route('/add_product', methods=['POST'])
def add_product():
  _code = request.form['code']
  _name = request.form['name']
  _price = int(request.form['price'])
  _image = request.form['image']
  _quantity = int(request.form['quantity'])
  # ข้อมูลของแต่ละแถวใน product_items

  row = {'code': _code, 'name': _name, 'price': _price,
    'image': _image, 'quantity': _quantity, 'total_price': _quantity * _price}
    
  # ตัวแปร session product_items ถูกสร้างแล้วหรือยัง ถ้ายังให้กำหนดให้ session['product_items'] เป็น dict ว่าง
  if not 'product_items' in session:
    session['product_items'] = {}

  # ถ้ามีสินค้านี้ในตะกร้าแล้ว
  if _code in session['product_items']:
        # อัพเดตจำนวน
    session['product_items'][_code]['quantity'] = session['product_items'][_code]['quantity'] + _quantity
    session['product_items'][_code]['total_price'] = session['product_items'][_code]['quantity'] * \
    session['product_items'][_code]['price']  # อัพเดตราคารวม
  else:
    # ถ้ายังไม่มีเพิ่มเข้าไป
    session['product_items'][_code] = row  # เพิิ่มแถวเข้าไป

  process_product_item()  # เรียกฟังชัน process_product_items เพื่อคำนวนณราคารวม และ หา product suggestion
  session.modified = True  # ให้ทำการเปลี่ยนแปลงค่าใน session แบบถาวร
  return ('', 204)

def process_product_item():
    if 'product_items' in session:
      all_total_quantity = 0
      all_total_price = 0
       # วิธีการวนลูปของ dictionary ใน ไพธอน
      for key, value in session['product_items'].items():
        individual_quantity = int(session['product_items'][key]['quantity'])
        individual_price = float(session['product_items'][key]['total_price'])
        all_total_quantity = all_total_quantity + individual_quantity
        all_total_price = all_total_price + individual_price

        session['all_total_quantity'] = all_total_quantity
        session['all_total_price'] = all_total_price

        suggestions = product_suggestion()
        # ถ้าจำนวนสินค้าที่แนะนำ > 0 เก็บไว้ใน sessions
        if(len(suggestions) > 0):
            session['suggestion'] = suggestions
        else:
          # ถ้าไม่ ลบ suggestion จาก session
            if 'suggestion' in session:
                session.pop('suggestion')

                
def powerset(iterable):
  s = list(iterable)
  return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))      
          
def product_suggestion():
  product_item = set()
  for key, value in session['product_items'].items():
    product_item.add(int(key))

  product_item_powerset = powerset(product_item)
  product_id_suggestions = set()  # สินค้าที่แนะนำทั้งหมด

  for s in product_item_powerset:
    # ค้นหาทุก subset ว่ามีตัวตรงกับ associaiotn rules
    antecedents = frozenset(s)
    if(rules and antecedents in rules):  # ถ้า match
      # อาจมีหลายกฎที่ ด้านหน้า (antecedent)เหมือนกัน เช่น (A,B) => (C,D) กับ (A,B)=>(X,Y)
      for r in rules[antecedents]:
      # ด้านหลัง consequent อาจมีสินค้ามากกว่า 1 ตัว (A,B) => (C,D) ดังนั้นเพิ่ม  C และ D ใน suggestions
        for m in r:
          product_id_suggestions.add(m)  # ถ้า match

  # ตัวที่แนะนำอาจซ้ำกับสิ่งที่อยู่ในตะกร้า
  # อ่านค่า product ในตะกร้า
  product_in_product_item = set()
  for key, value in session['product_items'].items():
    product_in_product_item.add(int(key))

  #ลบเซต : ให้เหลือแต่การแนะนำที่ยังไม่อยู่ในตะกร้า
  product_id_suggestions = product_id_suggestions - product_in_product_item

  # ใส่ข้อมูลของสินค้านอกเหนือจาก รหัสด้วย product_dict และเก็บไว้ใน list
  suggestions = list()
  for pid in list(product_id_suggestions):
    suggestions.append(product_dict[pid])

  return list(suggestions)

def encode_units(x):
  if x <= 0:
    return 0
  if x >= 1:
    return 1

def get_rules(min_support, min_confidence):
  try:
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT product_id,product_name,product_price,product_images FROM products')
    rows = cursor.fetchall()
    df_list = []
    for row in tqdm(rows):
      row_df = {'product_id': row[1], 'product_name': row[2], 'product_price': row[3]}
      df_list.append(row_df)

      df = pd.DataFrame(df_list)
      df.dropna(axis=0, subset=['product_id'], inplace=True)
      df['product_id'] = df['product_id'].astype('str')

      product_item = (df.groupby(['product_id', 'product_name'])['product_price'].sum().unstack().reset_index().fillna(0).set_index('id'))

      product_item_sets = product_item.applymap(encode_units)

      product_item_subsets = product_item_sets[:1000]

      frequent_itemsets = fpgrowth(product_item_subsets, min_support=min_support, use_colnames=True)
      a_rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_confidence)

      test_rules = {}
      for row in a_rules.iterrows():
        antecedents = row[1]['antecedents']
        consequents = row[1]['consequents']
        if antecedents not in test_rules:
          test_rules[antecedents] = []

          test_rules[antecedents].append(consequents)
        return test_rules

  except Exception as e:
    print(e)
def get_product_dict():
    try:
        result = dict()
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT  * FROM products")
        rows = cursor.fetchall()
        for row in rows:
            id = row['product_id']
            result[id] = row

        return result
    except Exception as e:
        print(e)

@app.route('/product_item_delete/<string:code>')
def delete_product_from_product_items(code):
  try:
    # pop ใช้ ลบค่าจาก dictionary
    # session.pop('product_items')
    session['product_items'].pop(code, None)
    process_product_item()  # จำนวนสินค้าหายไปดังนั้นให้คำนวนจำนวนเงินที่ต้องจ่ายใหม่
    return redirect('/shopping_cart')
  except Exception as e:
    print(e)


if __name__ == "__main__":
  rules = get_rules(min_support=0.05, min_confidence=0.8)
  product_dict = get_product_dict()  # 
  app.run(debug=True)