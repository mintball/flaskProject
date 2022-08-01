from flask import Flask, render_template
import pymysql

app = Flask(__name__)

# connect to database
conn = pymysql.connect(host='localhost', user='root', password='', db='product_db')
if conn:
    print('Connected to database')


@app.route('/')
def hello_world():  # put application's code here
    return render_template('show.html')


@app.route('/show')
def show_product():
    cur = conn.cursor()
    cur.execute('SELECT * FROM product')
    data = cur.fetchall()
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
