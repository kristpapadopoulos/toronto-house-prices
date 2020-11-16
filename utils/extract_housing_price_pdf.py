import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

url = "http://trreb.ca/index.php/market-news/mls-home-price-index/mls-home-price-index-archive"

folder_location = '/data/housing_price_pdf'

if not os.path.exists(folder_location):
    os.mkdir(folder_location)

response = requests.get(url)
soup= BeautifulSoup(response.text, "html.parser")  

years = []

for year_link in soup.select('h4'):
    
    year = year_link.text.strip(' ')
    
    years.append(year)
    
months = []

dec_list = []

for monthly_link in soup.select("a[href$='.pdf']"):
        
    month = monthly_link.text.strip(' ')
        
    if month in ['January','February','March','April','May','June','July',
                'August','September','October','November','December']:
        
        if month == 'December':
            dec_list.append(month)
            
        filename = f'{folder_location}/{years[len(dec_list)]}_{month}.pdf'
    
        with open(filename, 'wb') as f:
            f.write(requests.get(urljoin(url,monthly_link['href'])).content)