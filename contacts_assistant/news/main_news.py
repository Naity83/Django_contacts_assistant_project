import requests
from bs4 import BeautifulSoup
import json
import os
import datetime

# URL сайта, с которого собираем данные
url = "https://www.pravda.com.ua/"

def get_content(url):
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, "html.parser")
    news_items = soup.find_all('div', class_='article_header')
    news_data = []

    for news_item in news_items:
        try:
            title = news_item.find('h3').text.strip()
            article_url = news_item.find('a')['href']
            if article_url[0] != "h":
                article_url = "https://www.pravda.com.ua" + article_url

            # Убран парсинг даты, используем текущую дату
            published_date = datetime.date.today().strftime('%Y/%m/%d')

            news_data.append({
                'title': title,
                'url': article_url,
                'published_date': published_date  # Добавляем дату публикации
            })
        except Exception as e:
            # Убрана строка печати ошибки
            continue

    # Определяем путь к JSON-файлу относительно файла скрипта
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_file_path = os.path.join(base_dir, 'news', 'pravda_com_ua.json')

    # Очищаем данные в JSON файле перед записью новых данных
    with open(json_file_path, 'w', encoding='utf-8') as file:
        file.write("[]")

    # Сохраняем новые данные в файл JSON
    with open(json_file_path, 'w', encoding='utf-8') as file:
        json.dump(news_data, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    get_content(url)
