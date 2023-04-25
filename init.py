import sqlite3
import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import unquote, urlparse
from pathlib import PurePosixPath
connection = sqlite3.connect('database.db')
# using flask_restful
from flask import Flask, jsonify, render_template, request, url_for, flash, redirect
from flask_pymongo import PyMongo

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
app.config["MONGO_URI"] = "mongodb+srv://mayur:mayur@cluster0.zie9piv.mongodb.net/test"
mongodb_client = PyMongo(app)
db = mongodb_client.db
# db.api.delete_many({})
with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()
k = 1
for j in range(1,5):
        url = "https://www.discudemy.com/all"+'/'+str(j)
        response = requests.get(url)
        soup = bs(response.text, 'html.parser')
        rev_div = soup.findAll("div",attrs={"class":"content"})

        for i in rev_div:
            try:
                date = i.find(class_="label").text
                link = i.a['href']
                title = i.a.text
                # img = i.amp-img['src']
                images = i.find('div', attrs={"class":"img"})
                img = i.find('amp-img')['src']
                desc = i.find('div', attrs={'class':'description'}).text

            except:
                pass
            finally:
                if k % 2 == 0:
                    
                    a = PurePosixPath(
                        unquote(
                            urlparse(
                                link
                            ).path
                        )
                    ).parts[2]
                    url = "https://www.discudemy.com/go/"+str(a)
                    response = requests.get(url)
                    soup = bs(response.text, 'html.parser')
                    rev_div = soup.findAll("div",attrs={"class":"ui segment"})
                    for i in rev_div:
                        coupon = i.a['href']
                    db.api.insert_one({
                        'id': k,
                        'title': title,
                        'content': desc[2:-2],
                        'link': coupon,
                        'img': img,
                        'date': date
                    })
                    print("data inserted")
                    # cur.execute("INSERT INTO posts (title, content, link, img, date2) VALUES (?, ?,?,?,?)",(title, desc[2:-2],  coupon, img, date))
                else:
                    print("connot insert data")
                    pass
                    

            k+=1

connection.commit()
connection.close()