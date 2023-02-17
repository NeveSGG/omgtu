import requests
from bs4 import BeautifulSoup

def parse():
    url = "https://www.citilink.ru/catalog/smartfony/APPLE/"
    response = requests.get(url)
    print('Status code:', response.status_code)
    if(response.status_code!=200):
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    phones = {}
    try:
        for product in soup.find_all('div', {'class': 'ProductCardHorizontal'}):
            title = product.find('a', {'class': 'ProductCardHorizontal__title'}).text.strip()
            price = product.find('span', {'class': 'ProductCardHorizontal__price_current-price'}).text.strip().replace(' ', '').replace('₽', '')
            phones[title] = int(price)
    except:
        print('Ошибка во время парсинга')
        return

    for title, price in phones.items():
        print(title, ': ', price, '₽', sep='')

    print("Минимальная цена: ", min(phones.values()))
    print("Максимальная цена: ", max(phones.values()))
    print("Средняя цена: ", sum(phones.values()) / len(phones))

parse()