import pymysql
from flask import Flask, render_template
# Login
from flask_login import LoginManager,login_required

# create a flask application
app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

# connect to database
conn = pymysql.connect(host='localhost', user='root', password='', db='product_db')
if conn:
    print('Connected to database')


# Homepage
@app.route('/')
def Homepage():
    return render_template('index.html')


@app.route('/about')
def About():
    return render_template('about.html'), 404


@app.route('/contact')
def Contact():
    return render_template('contact.html'), 404


# Login page
@login_manager.user_loader
def load_user(user_id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cur.fetchone()
    cur.close()
    return user


@app.route('/login')
def Login():
    return render_template('auth/login.html')


# Dashboard page
@app.route('/dashboard')
@login_required
def Dashboard():
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run()
