from bs4 import BeautifulSoup
import requests
import csv
CSV = 'sulpak_smartphones.csv'
HOST = 'https://www.sulpak.kg/'
URL = 'https://www.sulpak.kg/f/smartfoniy'
HEADERS = {'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0'}

def get_html(URL,params=''):
    response = requests.get(URL, headers=HEADERS, params=params, verify=False)
    return response

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.findAll('div', class_='goods-tiles')
    smartphones = []


    for phones in items:
        smartphones.append({
                'title' : phones.find('h3', class_='title').get_text(strip=True),
                'price' : phones.find('div', class_='price-block').get_text(strip=True),
                # 'link' : HOST + phones.find('div', class_='goods-photo').find('webp').link.get('src'),
                'availability' : phones.find('span', class_='availability').get_text(strip=True)
            # 'link_page' : HOST + phones.find('a', class)
            #for link in soup.findAll('a'):
    # links.append(link.get('href'))
    #source type="image/webp"
        })
        return smartphones
    print('das')
def save(items, path):
    with open(path, 'a') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Название', 'Цена', 'Ссылка', 'наличие'])
        for item in items:
            writer.writerow([item['title'], item['price'],item['availability']])

def parser():
    PAGENATOR = input("Введите номер страницы: ")
    PAGENATOR = int(PAGENATOR.strip())
    html = get_html(URL)
    if html.status_code == 200:
        new_list = []
        for page in range(1, PAGENATOR):
            print(f"Страница №{page} готова")
            html = get_html(URL, params={'page':page})
            new_list.extend(get_content(html.text))
        save(new_list, CSV)
        print("Парсинг готов")
    else:
        print('error')

parser()



