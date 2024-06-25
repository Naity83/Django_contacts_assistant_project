import requests
from bs4 import BeautifulSoup
import datetime
import json
import os

# URL сайта, с которого собираем данные
url = "https://www.pravda.com.ua/"

def format_date():
    current_date = datetime.date.today()
    formatted_date = current_date.strftime("%Y/%m/%d")
    return formatted_date

current_date = format_date()

def get_content(url):
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, "html.parser")
    news_items = soup.find_all('div', class_='article_header')
    news_data = []

    for news_item in news_items:
        try:
            title = news_item.find('h3').text.strip()
            url = news_item.find('a')['href']
            if url[0] != "h":
                url = "https://www.pravda.com.ua" + url
            if current_date in url:
                news_data.append({
                    'title': title,
                    'url': url,
                    'published_date': current_date  # Добавляем текущую дату как дату публикации
                })
        except:
            continue

    # Определяем путь к JSON-файлу относительно файла скрипта
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_file_path = os.path.join(base_dir, 'news', 'pravda_com_ua.json')

    # Сохраняем данные в файл JSON
    with open(json_file_path, 'w', encoding='utf-8') as file:
        json.dump(news_data, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    get_content(url)








