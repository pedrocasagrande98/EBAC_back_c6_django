import factory
from faker import Factory as FakerFactory
from .models import Contact

faker = FakerFactory.create()

class ContactFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Contact

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    phone_number = factory.Faker("phone_number")
    email = factory.Faker("safe_email")
