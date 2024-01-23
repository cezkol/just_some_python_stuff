#Simple scrapper for polish Pan Tu Nie Stał shop, which collects all currently discounted items
#and store them in ptns database


from time import sleep
from requests import get
from bs4 import BeautifulSoup
import sqlite3

#input data
base_url="https://pantuniestal.com/pl/promotions/"
page_number=1   #start srcapping from
products_list=[]    #list of scrapped items
old_data=None

#data base creation
#table consists 3 columns: name of item, item category and price
conn=sqlite3.connect("ptns.db")
c=conn.cursor()
c.execute("DROP TABLE IF EXISTS promo")
c.execute('''CREATE TABLE promo (
	name TEXT,
	category TEXT,
	price REAL
	);''')
conn.commit()
query_item=f"INSERT INTO promo VALUES (?,?,?);"

#scrapping loop
while True:
	res=get(base_url+str(page_number))
	soup=BeautifulSoup(res.text, "html.parser")
	new_data=soup.find_all(class_="product-inner-wrap")

    #shop webpage is constructed in such a way, that if https://pantuniestal.com/pl/promotions/n page doesn't exist,
    #it will automatically redirect you to the last page of /promotions/ section
    #so if new scrapped data are the same as old data, it means that we are on the last page of promotions and loop breaks
	if old_data==new_data:
		break

	products_list.extend(new_data)
	old_data=new_data
	page_number+=1
	sleep(1)

#filling the database
for item in products_list:
	name=item.find("a")["title"]
	category=item.parent["data-category"]
	price=float(item.find(class_="price pricecustom row").find("em").get_text()[:-3].replace(",", "."))
	data=(name, category, price)
	c.execute(query_item, data)
	conn.commit()

conn.close()