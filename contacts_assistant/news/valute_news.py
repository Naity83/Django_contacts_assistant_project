import requests
import json
from datetime import datetime
import os

def get_exchange_rates():
    today_date = datetime.now().strftime('%d.%m.%Y')
    url = f'https://api.privatbank.ua/p24api/exchange_rates?json&date={today_date}'
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на успешный HTTP-ответ
        data = response.json()

        # Фильтруем данные для USD, EUR и PLN
        filtered_data = {
            "date": data["date"],
            "bank": data["bank"],
            "baseCurrency": data["baseCurrency"],
            "baseCurrencyLit": data["baseCurrencyLit"],
            "exchangeRate": []
        }

        for item in data["exchangeRate"]:
            if item["currency"] in ["USD", "EUR", "PLN"]:
                filtered_data["exchangeRate"].append(item)

        # Определяем путь к JSON-файлу относительно файла скрипта
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        json_file_path = os.path.join(base_dir, 'news', 'valute.json')

        # Очищаем данные в JSON файле перед записью новых данных
        with open(json_file_path, 'w', encoding='utf-8') as file:
            file.write("[]")

        # Сохраняем отфильтрованные данные в файл JSON
        with open(json_file_path, 'w', encoding='utf-8') as file:
            json.dump(filtered_data, file, ensure_ascii=False, indent=4)

        return filtered_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

if __name__ == "__main__":
    get_exchange_rates()


