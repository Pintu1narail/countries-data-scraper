import csv
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://google.com'
}

country_list = []

url = 'https://www.scrapethissite.com/pages/simple/'

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    countries = soup.find_all('div', class_='col-md-4')

    for country in countries:
        name = country.find('h3', class_='country-name').text.strip()
        capital = country.find('span', class_='country-capital').text.strip()
        population = country.find('span', class_='country-population').text.strip()
        area = country.find('span', class_='country-area').text.strip()

        country_list.append({
            'Country Name': name,
            'Capital': capital,
            'population': population,
            'Area': area
        })

else:
    print(f"Data not found! Error code : {response.status_code}")

df = pd.DataFrame(country_list)
df.to_csv('Country.csv', index=False, encoding='utf-8')
print(df.head())
