from flask import Flask,render_template

app = Flask(__name__)

@app.route("/index")
def index():
  return render_template('index.html')

@app.route("/manga_best_seller")
def manga_best_seller():
  return render_template('manga_best_seller.html')

@app.route("/signin")
def signin():
  return render_template('signin.html')

@app.route("/signup")
def signup():
  return render_template('signup.html')

if __name__ == "__main__":
  app.run(debug=True)