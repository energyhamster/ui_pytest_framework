from faker import Faker

from data.data import Person

faker_en = Faker('en_US')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_en.first_name() + " " + faker_en.last_name(),
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        age=faker_en.random.randint(10, 80),
        department=faker_en.job(),
        salary=faker_en.random.randint(1000, 8000),
        email=faker_en.email(),
        current_address=faker_en.street_address(),
        permanent_address=faker_en.street_address(),
    )
