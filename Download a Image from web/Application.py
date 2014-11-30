__author__ = 'Aman'
# we are saving files using random name so we will import random
import random
import urllib.request
def download_web_image(url) :
    name = random.randrange(1,1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url,full_name)
download_web_image("http://4.bp.blogspot.com/-F6FiMfAtbiY/UGsOUZs0oMI/AAAAAAAAHoE/MyQgHUNBg6w/s1600/JULIAN+CHARRIE%CC%80RE+TRIANGULATION+BLOG+2.jpeg")