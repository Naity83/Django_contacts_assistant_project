import random
from faker import Faker

from contacts.models import Contact

fake = Faker()

def create_fake_contact():
    contact = Contact(
        full_name=fake.name(),
        phone_number=fake.phone_number(),
        address=fake.address(),
        birthday=fake.date_of_birth(minimum_age=18, maximum_age=90),
        email=fake.email()
    )
    contact.save()

def populate_contacts(n=50):
    for _ in range(n):
        create_fake_contact()
    print(f'{n} fake contacts have been created.')

if __name__ == '__main__':
    populate_contacts()
