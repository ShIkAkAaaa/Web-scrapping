import bs4
import requests

KEYWORDS = ['дизайн', 'фото', 'web', 'python']
URL = "https://habr.com/ru/all/"

response = requests.get(URL)
text = response.text

soup = bs4.BeautifulSoup(text, features="html.parser")

articles = soup.find_all("article")

for article in articles:
    date = article.find('time').get('title')
    caption = article.find('h2').find('span').text
    href = article.find('h2').find('a').get('href')
    print(f'{date} - {caption} - https://habr.com{href}')