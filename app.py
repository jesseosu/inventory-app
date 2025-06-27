from flask import Flask, render_template, request, redirect
import mysql.connector
import os

app = Flask(__name__)

# db_config = {
#     'host': os.environ.get('DB_HOST'),
#     'user': os.environ.get('DB_USER'),
#     'password': os.environ.get('DB_PASSWORD'),
#     'database': os.environ.get('DB_NAME')
# }

@app.route('/')
def index():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM inventory")
    items = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    quantity = request.form['quantity']
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s)", (name, quantity))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
