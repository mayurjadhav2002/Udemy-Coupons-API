# using flask_restful
from flask import Flask, jsonify, render_template, request, url_for, flash, redirect

import requests
from bs4 import BeautifulSoup as bs
import sqlite3
import json
import os
from flask_cors import CORS

# creating the flask app
app = Flask(__name__)

CORS(app)
# creating an API object

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Connection Creator and Fetch the Content from database
conn = get_db_connection()
posts = conn.execute('SELECT * FROM posts').fetchall()
conn.close()
data = posts
k = 0
jsondata=[]
for i in data:
    k+=1
    jsondata.append({
                'id': i['id'],
                'title': i['title'],
                'img': i['img'],
                'description':i['content'],
                'link':i['link'],
                'date':i['date2'],
            
    })
# Index Page / Home Page
@app.route('/')           
@app.route('/data')
def index():
    return jsonify(jsondata)

# showing the only one row from database
@app.route('/data/<int:id>')
def show_all(id):
    if id < 60:
        return jsonify([jsondata[id]])
    else:
        return "{'result':'No data Found'}"
 
# 404 Not Found Page
@app.errorhandler(404)
def not_found(e):
    return "Page Not Found"


# Admin page to update the data
@app.route('/admin/update_data/', methods=('GET', 'POST'))
def home():
    if request.method == 'POST':
        title = request.form['title']
        password = request.form['password']
        if not title:
            flash('Title is required!')
        elif not password:
            flash('password is required!')
        else:
            # Enter your email and password here, you can include any letters at the place of email
            if title=="Email" and password=="password":
                os.system('python init.py')
                return "<h1>Data Updated</h1>"
    return render_template('home.html')


# Delete the not working Coupon Codes
@app.route("/delete/<int:id>")
def delete(id):
        jsondata.pop(id)
        # sqliteConnection = sqlite3.connect('database.db')
        # cursor = sqliteConnection.cursor()
        # sql_delete_query = """DELETE from posts where id = ?"""
        # cursor.execute(sql_delete_query, (id,))
        # sqliteConnection.commit()
        # cursor.close()
        # sqliteConnection.close()
        return "[{'message': 'Record Removed'}]"
# driver function
if __name__ == '__main__':
    try:
        db.session.query(model_name).delete() 
        db.session.commit()
        
    except:
        pass
    finally:
           db.create_all()
           app.run(debug=True, host='0.0.0.0', port='5000')