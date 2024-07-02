from django.core.management.base import BaseCommand
from contacts.models import Contact
from faker import Faker

class Command(BaseCommand):
    help = 'Populates the database with fake contacts'

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(5):
            Contact.objects.create(
                full_name=fake.name()[:200],  # Ограничение длины до 200 символов
                address=fake.address()[:255],  # Ограничение длины до 255 символов
                phone_number=fake.phone_number()[:15],  # Ограничение длины до 15 символов
                email=fake.email(),
                birthday=fake.date_of_birth(),
                user_id=1  # Пример ID пользователя
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated contacts'))