import pandas as pd
from bs4 import BeautifulSoup
import requests
import pymysql

# URL to scrape data from
link = "https://www.flipkart.com/search?q=mobiles"
req = requests.get(link)
soup = BeautifulSoup(req.content, "html.parser")

# Extracting data
mob_name = soup.find_all("div", class_="KzDlHZ")
mob_ratings = soup.find_all("div", class_="XQDdHH")
mob_ram = soup.find_all("div", class_="_6NESgJ")
mob_offers = soup.find_all("div", class_="n5vj9c")

# Lists to store the data
a = []
b = []
c = []
d = []

# Iterating over the extracted data
for cost, offer, name, rating in zip(mob_name, mob_offers, mob_ram, mob_ratings):
    a.append(name.text)
    b.append(rating.text)
    c.append(offer.text)
    d.append(cost.text)

# Creating a DataFrame
data = {'name': a, 'rating': b, 'offers': c, 'cost': d}
flipkart = pd.DataFrame(data)

# MySQL database connection
db = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='akhil',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = db.cursor()

# Creating the table if it does not exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS mobiles (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name LONGTEXT,
        rating TEXT,
        offers TEXT,
        cost TEXT
    )
""")

# Inserting data into the database
for index, row in flipkart.iterrows():
    cursor.execute("""
        INSERT INTO mobiles (name, rating, offers, cost)
        VALUES (%s, %s, %s, %s)
    """, (row['name'], row['rating'], row['offers'], row['cost']))

# Committing the transaction
db.commit()

# Closing the connection
cursor.close()
db.close()

# Saving the DataFrame to a CSV file
flipkart.to_csv("mob_data.csv", index=False)

# Printing the DataFrame
print(flipkart)
