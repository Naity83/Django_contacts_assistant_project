from django.shortcuts import render
import os
import json
import datetime
from .main_news import get_content 
from .valute_news import get_exchange_rates
from .models import Article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    url = "https://www.pravda.com.ua/"
    
    # Очищаем таблицу в базе данных перед добавлением новых данных
    Article.objects.all().delete()
    
    # Собираем свежие данные с сайта
    get_content(url)
    valute_data = get_exchange_rates()  # Получаем данные о курсах валют

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_file_path = os.path.join(base_dir, 'news', 'pravda_com_ua.json')

    try:
        # Читаем свежие данные из JSON файла
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        for item in data:
            published_date = datetime.datetime.strptime(item['published_date'], "%Y/%m/%d").date()
            Article.objects.create(
                title=item['title'], 
                url=item['url'],
                published_date=published_date
            )

        # Получаем список всех статей
        article_list = Article.objects.all()

        # Пагинация для новостей
        paginator = Paginator(article_list, 9)
        page_number = request.GET.get('page')
        try:
            articles = paginator.page(page_number)
        except PageNotAnInteger:
            articles = paginator.page(1)
        except EmptyPage:
            articles = paginator.page(paginator.num_pages)

        context = {
            'valute_data': valute_data,
            'articles': articles,
        }
        return render(request, 'news/news.html', context)

    except FileNotFoundError:
        return render(request, 'news/news.html', {'error': 'Файл с новостями не найден.'})
    except json.JSONDecodeError:
        return render(request, 'news/news.html', {'error': 'Ошибка декодирования JSON файла.'})
