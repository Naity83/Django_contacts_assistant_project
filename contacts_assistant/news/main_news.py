import requests
from bs4 import BeautifulSoup
import datetime
import json

# URL сайту, з якого ми збираємось скрапити дані
url = "https://www.pravda.com.ua/"

def format_date():
    curent_data = datetime.date.today()
    formatted_date = curent_data.strftime("%Y/%m/%d")
    return formatted_date


curent_data = format_date() # потрібний формат дати Приклад: 2024/06/24

def get_contetnt(url):

    # Надсилаємо HTTP-запит до сайту та отримуємо HTML-сторінку
    resp = requests.get(url)
    html_content = resp.content

    # Аналізуємо HTML-сторінку за допомогою BeautifulSoup
    soup= BeautifulSoup(html_content, "html.parser")

    # Знаходимо всі потрібні нам елементи новин на сторінці
    news_items = soup.find_all('div', class_='article_header')

    # Створюємо список для збереження новинної інформації
    news_data = []

    #Перебираємо кожен елемент новини та витягуємо необхідну інформацію
    for news_item in news_items:
        try :
    # print(news_item.text)
            title = news_item.find('h3').text.strip()
            url = news_item.find('a')['href']
        
            if url[0] != "h":
                        url = "https://www.pravda.com.ua"+ url
                    # print(f"url= {url}")
            if curent_data in url :

    # # Додаємо інформацію про новину до списку
       
                    news_data.append({'title': title,'url': url})
        except:
            continue
    # Зберігаємо дані у файл у форматі JSON    
    with open('pravda_com_ua.json', 'w', encoding='utf-8') as file:
            json.dump(news_data, file, ensure_ascii=False, indent=4)

            print('Дані успішно збережено у файл "news_data.json".')
    if not news_items:
            print("Не вдалося знайти жодних новин на сторінці.")




if __name__ == "__main_news__" :

    # parset_contetnt(url)
    get_contetnt(url)














