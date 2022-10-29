import sqlite3
import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import unquote, urlparse
from pathlib import PurePosixPath
connection = sqlite3.connect('database.db')


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
                    cur.execute("INSERT INTO posts (title, content, link, img, date2) VALUES (?, ?,?,?,?)",(title, desc[2:-2],  coupon, img, date))
                else:
                    pass

            k+=1

connection.commit()
connection.close()