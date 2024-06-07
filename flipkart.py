# import pandas as p
# from bs4 import BeautifulSoup
# import requests
# import csv

# link="https://www.flipkart.com/search?q=mobiles"
# req=requests.get(link)
# soup=BeautifulSoup(req.content,"html.parser")
# lap_name=soup.find_all("div",class_="VU-ZEz")
# lap_ratings=soup.find_all("div",class_="E3XX7J")
# lap_offers=soup.find_all("span",class_="pu8Q93")
# lap_cost=soup.find_all("div",class_="hl05eU")

# a=[]
# b=[]
# c=[]
# d=[]
# for naam,ratings,review,cost in zip(lap_cost,lap_offers,lap_name,lap_ratings):
#     a.append(naam.text)
#     b.append(ratings.text)
#     c.append(review.text)
#     d.append(cost.text)

# # e={a:"naam",b:"ratings",c:"review",d:"cost"}
# e={"naam":a,"ratings":b,"review":c,"cost":d}
# flipkart=p.DataFrame(data=e)
# flipkart.to_csv("lap_data.csv")

# print(lap_name)






















































# # import pandas as pd
# # from bs4 import BeautifulSoup
# # import requests

# # # Correct link to a specific Flipkart laptop page
# # link = "https://www.flipkart.com/acer-intel-core-i3-13th-gen-1315u-8-gb-256-gb-ssd-chrome-os-chromebook-plus/p/itmd8a0bdb25419a?pid=COMHFC9KY8AHGYD3&lid=LSTCOMHFC9KY8AHGYD3YI3XV7&marketplace=FLIPKART&q=laptops&store=6bo%2Fb5g&srno=s_1_2&otracker=AS_Query_TrendingAutoSuggest_9_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_9_0_na_na_na&fm=organic&iid=en_g3paUJp98ne-HOrmm9ptI2zPee09vz6ubHlm5LBgb0d5GEXbB3uLzLqwD87yOuAht3UnPZLFTXA6cvt8bwe46_UFjCTyOHoHZs-Z5_PS_w0%3D&ppt=sp&ppn=sp&ssid=sfow47s3n40000001717673024615&qH=c06ea84a1e3dc3c6"
# # req = requests.get(link)
# # soup = BeautifulSoup(req.content, "html.parser")

# # # Inspect the HTML to find the correct class names
# # lap_name = soup.find_all("span", class_="B_NuCI")  # Name class
# # lap_ratings = soup.find_all("div", class_="_3LWZlK")  # Ratings class
# # lap_offers = soup.find_all("div", class_="_16FRp0")  # Offers class
# # lap_cost = soup.find_all("div", class_="_30jeq3 _16Jk6d")  # Cost class

# # # Initialize lists to store the scraped data
# # a = []
# # b = []
# # c = []
# # d = []

# # # Collect data from the parsed HTML
# # for name, ratings, offers, cost in zip(lap_name, lap_ratings, lap_offers, lap_cost):
# #     a.append(name.text)
# #     b.append(ratings.text)
# #     c.append(offers.text)
# #     d.append(cost.text)

# # # Check if the lists are populated correctly
# # print("Names: ", a)
# # print("Ratings: ", b)
# # print("Offers: ", c)
# # print("Costs: ", d)

# # # Create a dictionary to pass to the DataFrame
# # e = {
# #     "Name": a,
# #     "Rating": b,
# #     "Offers": c,
# #     "Cost": d
# # }

# # # Create a DataFrame from the dictionary
# # flipkart = pd.DataFrame(data=e)

# # # Save the DataFrame to a CSV file
# # flipkart.to_csv("lap_data.csv", index=False)













import pandas as pd
from bs4 import BeautifulSoup
import requests
import csv
link = "https://www.flipkart.com/search?q=mobiles"
req = requests.get(link)
soup = BeautifulSoup(req.content, "html.parser")
mob_name = soup.find_all("div", class_="KzDlHZ")
mob_ratings = soup.find_all("div", class_="XQDdHH")
mob_ram = soup.find_all("div", class_="_6NESgJ")
mob_offers = soup.find_all("div", class_="n5vj9c")
a=[]
b=[]
c=[]
d=[]
for cost, offer, name, rating in zip(mob_name, mob_offers, mob_ram, mob_ratings):
    a.append(name.text)
    b.append(rating.text)
    c.append(offer.text)
    d.append(cost.text)
e= {'a': a, 'b': b, 'c': c, 'd': d}
print(e)
flipkart = pd.DataFrame(data=e)
flipkart.to_csv("mob_data.csv", index=False)
print(flipkart)



































# import pandas as pd
# from bs4 import BeautifulSoup
# import requests
# import csv

# # URL of the Flipkart search page for mobiles
# link = "https://www.flipkart.com/search?q=mobiles"
# req = requests.get(link)
# soup = BeautifulSoup(req.content, "html.parser")

# # Lists to store the scraped data
# names = []
# ratings = []
# ram_rom = []
# offers = []

# # Find all the mobile listings
# mobiles = soup.find_all("div", class_="_1AtVbE")

# # Loop through each mobile listing and extract the required details
# for mobile in mobiles:
#     # Extract the name of the mobile
#     name_tag = mobile.find("div", class_="_4rR01T")
#     if name_tag:
#         names.append(name_tag.text)
#     else:
#         names.append(None)

#     # Extract the rating of the mobile
#     rating_tag = mobile.find("div", class_="_3LWZlK")
#     if rating_tag:
#         ratings.append(rating_tag.text)
#     else:
#         ratings.append(None)

#     # Extract the RAM/ROM details
#     ram_rom_tag = mobile.find("ul", class_="_1xgFaf")
#     if ram_rom_tag:
#         ram_rom.append(ram_rom_tag.text)
#     else:
#         ram_rom.append(None)

#     # Extract the offer details
#     offer_tag = mobile.find("div", class_="_3Ay6Sb")
#     if offer_tag:
#         offers.append(offer_tag.text)
#     else:
#         offers.append(None)

# # Create a DataFrame with the scraped data
# data = {
#     'Name': names,
#     'Rating': ratings,
#     'RAM_ROM': ram_rom,
#     'Offers': offers
# }

# flipkart_df = pd.DataFrame(data)
# # print(flipkart_df)

# # Save the DataFrame to a CSV file
# flipkart_df.to_csv("mob_datas.csv", index=False)























# import pandas as pd
# from bs4 import BeautifulSoup
# import requests

# # Correct link to Flipkart laptops page
# link = "https://www.flipkart.com/acer-swift-go-14-evo-oled-intel-core-i5-13th-gen-13500h-16-gb-512-gb-ssd-windows-11-home-sfg14-71-58ub-thin-light-laptop/p/itm0a080194d6dd1?pid=COMGZKGGAHZBA3WY&lid=LSTCOMGZKGGAHZBA3WYWOBYJC&marketplace=FLIPKART&store=6bo%2Fb5g&srno=b_1_1&otracker=browse&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_8_L1_view-all&fm=organic&iid=en_6cAMdjM00VC0NN2YUxGX9bnjyrJAz8WYQfCMdxvwNO9wBKkBthdMKn_IDmg2ZpUmIzsgGpa5cchBYc2PC5S2NfUFjCTyOHoHZs-Z5_PS_w0%3D&ppt=hp&ppn=homepage&ssid=1l2gyeugk00000001717666662542"

# # Send a request to the webpage
# req = requests.get(link)
# soup = BeautifulSoup(req.content, "html.parser")

# # Inspect the HTML to find the correct class names
# lap_name = soup.find_all("div", class_="_4rR01T")  # Update with the correct class name for laptop names
# lap_ratings = soup.find_all("div", class_="_3LWZlK")  # Update with the correct class name for ratings
# lap_review = soup.find_all("span", class_="_2_R_DZ")  # Update with the correct class name for reviews
# lap_cost = soup.find_all("div", class_="_30jeq3 _1_WHN1")  # Update with the correct class name for cost

# # Initialize lists to store the scraped data
# a = []
# b = []
# c = []
# d = []

# # Collect data from the parsed HTML
# for name, ratings, review, cost in zip(lap_name, lap_ratings, lap_review, lap_cost):
#     a.append(name.text)
#     b.append(ratings.text)
#     c.append(review.text)
#     d.append(cost.text)

# # Check if the lists are populated correctly
# print("Names: ", a)
# print("Ratings: ", b)
# print("Reviews: ", c)
# print("Costs: ", d)

# # Create a dictionary to pass to the DataFrame
# e = {
#     'Name': a,
#     'Rating': b,
#     'Review': c,
#     'Cost': d
# }

# # Create a DataFrame from the dictionary
# flipkart = pd.DataFrame(data=e)

# # Save the DataFrame to a CSV file
# flipkart.to_csv("lap_data.csv", index=False)


