import requests, re
from bs4 import BeautifulSoup

# open URL.txt
# save visited page's URL
# URL
addr='http://www.sogang.ac.kr/bachelor/index.html'
#scraper function
def scraper(url):
    try:
#get url using requests
        r = requests.get(url)
#error if could not get instruction
        if r.ok == False:
            return
        elif r.ok == True and r.status_code != 404 and r.status_code != 403 and r.status_code != 401:
#using beautifulsoup api
            b = BeautifulSoup(r.content,'html.parser')
#count for the number of files
            print(b)
        else:
            print('Error with protocol')
            return
    except:
        print('Exception error')
        return

# call scraper
scraper(addr)

