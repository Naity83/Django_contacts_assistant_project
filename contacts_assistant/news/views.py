from django.shortcuts import render
import os
import json
import datetime
from .main_news import get_content 

# Create your views here.
from .models import Article

def index(request):
    url = "https://www.pravda.com.ua/"
    get_content(url)
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_file_path = os.path.join(base_dir, 'news', 'pravda_com_ua.json')

    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        for item in data:
            published_date = datetime.datetime.strptime(item['published_date'], "%Y/%m/%d").date()
            article, created = Article.objects.get_or_create(
                title=item['title'], 
                url=item['url'],
                defaults={'published_date': published_date}
            )
            if created:
                article.save()

        articles = Article.objects.all()
        return render(request, 'news/news.html', {'articles': articles})
    except FileNotFoundError:
        return render(request, 'news/news.html', {'error': 'Файл с новостями не найден.'})
    except json.JSONDecodeError:
        return render(request, 'news/news.html', {'error': 'Ошибка декодирования JSON файла.'})