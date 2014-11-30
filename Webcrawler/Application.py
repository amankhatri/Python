import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1

    while page < max_pages:
        url = 'https://buckysroom.org/trade/search.php?page='+str(page)
        source_code = requests.get(url)  # gets the source code
        plain_text = source_code.text  # extracts the plain text only
        #Now we will convert it into beautiful soup object
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a', {'class': 'item-name'}):  # here 'a' is for the links
            href = 'https://www.thenewboston.com'+link.get('href')
            title = link.string
            print(href)
            print(title)
            get_single_item_data(href)
        print("outta loop")
        page += 1
def get_single_item_data(item_url):
     source_code = requests.get(item_url)  # gets the source code
     plain_text = source_code.text  # extracts the plain text only
        #Now we will convert it into beautiful soup object
     soup = BeautifulSoup(plain_text)
     for item_name in soup.find_all('div',{'class':'i-name'}):  #for each loop soup.findall(tag,class:classname})
         print(item_name.string)
     #find all the links on the page
     for link in soup.find_all('a'):
         href = 'https://www.thenewboston.com'+link.get('href')
         print(href)
         # if we don't want to print the same links again and again we can use a set

trade_spider(2)