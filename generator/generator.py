import random

from faker import Faker

from data.data import Person, Color

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
        mobile=faker_en.msisdn(),
    )


def generated_file():
    path = rf"C:\code\test\pythonCode\pythonProject\ui_pytest_framework\file_test{random.randint(0, 999)}.txt"
    file = open(path, "w+")
    file.write(f"Hello World{random.randint(0, 999)}")
    file.close()
    return file.name, path


def generated_subject():
    subject_list = ["Hindi", "English", "Maths", "Physics", "Chemistry", "Biology", "Computer Science", "Commerce",
                    "Accounting", "Economics", "Arts", "Social Studies", "History", "Civics"]
    return subject_list[random.randint(0, len(subject_list) - 1)]


def generated_state_and_city():
    state_list = ["NCR", "Uttar Pradesh", "Haryana", "Rajasthan"]
    state = state_list[random.randint(0, len(state_list) - 1)]

    city_dict = {
        "NCR": ("Delhi", "Gurgaon", "Noida"),
        "Uttar Pradesh": ("Agra", "Lucknow", "Merrut"),
        "Haryana": ("Karnal", "Panipat"),
        "Rajasthan": ("Jaipur", "Jaiselmer")
    }
    city_tuple = city_dict[state]
    city = city_tuple[random.randint(0, len(city_tuple) - 1)]
    return state, city


def generated_color():
    yield Color(
        color_name=["Red", "Blue", "Green", "Yellow", "Purple", "Black", "White", "Voilet", "Indigo", "Magenta", "Aqua"]
    )
