__author__ = 'kaman'
#we will crawl a webpage and then count the number of times each word is repeated
import requests
import  operator
from bs4 import BeautifulSoup

def start(url):
    #creating a blank list
    word_list = []
    #we will get the source code from the website and put it in wordlist
    source_code = requests.get(url).text #connect to url and pull everything as text
    #whenever you have Beautiful soup you want to convert everything into soup
    soup = BeautifulSoup(source_code)
    for post_text in soup.find_all('a',{'class':'index_singleListingTitles'}) : #'links', properties
        content = post_text.string #ignore all html from now and get the text as string
        #lower case everything in the string or the sentence in content and splits it using space
        words = content.lower().split()
        for each_word in words:
            word_list=word_list.append(each_word)
            print(word_list)
    clean_up_list(word_list)

def clean_up_list(list_of_words):
    clean_word_list = []  #remove all the dots and the other special chars
    for word in list_of_words :
        #list of symbols to take out
        symbols="!@#$%^&*():\"<>,./;'[]-*"
        for i in range(0,len(symbols)):
            word = word.replace(symbols[i],"")
        #if the lengh of the word is greater than 0 only than add the word to the list
            if len(word):
                clean_word_list.append(word)
    create_dictonary(clean_word_list)
#now we are creating a dictionary with the information about how many times have a single word been repeaded
def create_dictonary(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
                word_count[word] +=1
        else:
                word_count[word] =1
    #sorting dictionary based on frequency of words appearring
    for key,value in sorted(word_count.items(),key = operator.itemgetter(1)):
        print(key,value)



start('https://www.thenewboston.com/tops.php?type=text&period=this-month')