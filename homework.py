import bs4
import requests

HUBS = ['дизайн', 'фото', 'web', 'python', 'Процессоры', 'Киберпанк', 'Физика', 'Программирование']


url = 'https://habr.com/ru/all/'
url_two = 'https://habr.com'

response = requests.get(url,
                        headers={'User-Agent': 'Mozilla/5.0 '
                                               '(Windows NT 10.0; Win64; x64) '
                                               'AppleWebKit/537.36 (KHTML, like Gecko) '
                                               'Chrome/101.0.4951.54 Safari/537.36'})
response.raise_for_status()
text = response.text
soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')

for article in articles:
    hubs = article.find_all(class_='tm-article-snippet__hubs-item')
    hubs = set(hub.text.strip() for hub in hubs)
    for hub in hubs:
        if hub in HUBS:
            dat = article.find(class_='tm-article-snippet__datetime-published').time['title']
            name = article.find(class_='tm-article-snippet__title tm-article-snippet__title_h2').text
            href = article.find(class_='tm-article-snippet__title tm-article-snippet__title_h2').a['href']
            print(dat, '-', name, '-', url_two + href)
