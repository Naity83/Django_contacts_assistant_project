import json
from django.shortcuts import render
from .models import Article

def index(request):
    with open('pravda_com_ua.json', 'r') as file:
        data = json.load(file)
    
    # Створюємо нові записи в базі даних
    for item in data:
        article = Article(title=item['title'], url=item['url'])
        article.save()
    
    articles = Article.objects.all()
    return render(request, 'news/news.html', {'articles': articles})