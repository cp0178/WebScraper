import requests
import sys
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
from fake_useragent import UserAgent
#takes in an argument from the command line
url = sys.argv[1]

#print(url)
#gets details of the Amazon page
def get_details(url):
    #tries different user agents
    ua = UserAgent()
    uaRandom = ua.random
    header = {
        'User-Agent': uaRandom,
        'Accept-Language': 'en-US,en;q=0.9'
    }
    
    isCaptcha = True
    while isCaptcha:
        page = requests.get(url, headers=header)
        #sees if it connected
        assert page.status_code == 200
        soup = BeautifulSoup(page.content,'lxml')
        #checks if the page detects is a bot
        if 'captcha' in str(soup):
            uaRandom = ua.random
            print(f'\rBot has been detected... retrying ... use new identity: {uaRandom} ', end='', flush=True)
            #itterates through 
            continue
        else:
            #prints the price of an object
            print('Got through')
            string = str(soup.find_all(class_="a-price-whole"))
            string = re.sub("<.*?>", " ", string)
            index = string.find('.')
            string = string[2 : index]
            priceString = "Price: " + string
            return priceString
            
            

print(get_details(url))

