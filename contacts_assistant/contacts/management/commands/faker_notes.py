# scripts/populate_data.py

import random
from faker import Faker
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from notes.models import Note, Tag

class Command(BaseCommand):
    help = 'Populate database with fake notes and tags'

    def handle(self, *args, **kwargs):
        fake = Faker()
        users = User.objects.all()  # Получаем всех пользователей, у вас может быть свой способ получения пользователей

        for _ in range(20):  # Создаем 20 фейковых записей
            user = random.choice(users)
            name = fake.text(max_nb_chars=50)  # Генерируем случайное имя для записи
            description = fake.text(max_nb_chars=150)  # Генерируем случайное описание

            note = Note.objects.create(name=name, description=description, user=user)

            # Добавляем случайное количество тегов к записи (от 1 до 3 тегов)
            for _ in range(random.randint(1, 3)):
                tag_name = fake.word()  # Генерируем случайное имя тега
                tag, created = Tag.objects.get_or_create(name=tag_name, user=user)
                note.tags.add(tag)

            self.stdout.write(self.style.SUCCESS(f'Created note "{note.name}"'))

        self.stdout.write(self.style.SUCCESS('Successfully populated database with fake data'))
