import requests
from bs4 import BeautifulSoup as BS
import time

#парсинг крипты


while True:
    url = "https://www.rbc.ru/crypto/currency/btcusd/"
    html = requests.get(url)
    soup = BS(html.text, "html.parser")
    value = soup.find("div", class_="chart__subtitle js-chart-value")
    value.span.decompose()

    for items in value:
        if items != "\n":
            print(f'Цена BTC: {items.replace(" ", "").strip()}')
        time.sleep(3)




