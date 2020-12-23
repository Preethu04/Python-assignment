import requests
from bs4 import BeautifulSoup
import pprint


def strip_html(url):

    try:
        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text, 'html.parser')
        
        return (soup.get_text().strip())
    
    except:

        return 'Invalid URL'

if __name__ == '__main__':

    print(strip_html('https://www.datagrokr.com/'))

