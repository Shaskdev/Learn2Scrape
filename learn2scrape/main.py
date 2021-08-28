import requests
from bs4 import BeautifulSoup

page = requests.get("https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(page.content, 'html.parser')
page_title = soup.title.text

page_head = soup.head
page_body = soup.body

#selecting DOM elements using .select 
all_h1_tags = soup.select('h1')
seventh_p_text = soup.select('p')[6]
all_images = soup.find_all("img")

top_items = soup.select("a.title")
item_ratings = soup.select('div.ratings')



print(page_title)