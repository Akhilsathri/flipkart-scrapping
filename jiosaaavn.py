import csv
import requests
from bs4 import BeautifulSoup
import pandas as p

link=("https://www.myntra.com/watches-?rawQuery=watches%20")
req=requests.get(link)
soup=BeautifulSoup(req.content,"html.parser")
watch_img=soup.find_all("img",class_="_53J4C-")
watch_price=soup.find_all("div",class_="Nx9bqj")
watch_discount=soup.find_all("div",class_="UkUFwK")
a=[]
b=[]
c=[]
for img,price,disc in zip(watch_img,watch_discount,watch_price):
    a.append(img.text)
    b.append(price.text)
    c.append(disc.text)
d={'a':a,'b':b,'c':c}
result=p.DataFrame(data=d)
result.to_csv("meesho.csv")

print(result)

