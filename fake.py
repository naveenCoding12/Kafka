from faker import Faker

import json

fake = Faker()

def generate_fake_pizza():
    pizza_name = fake.word()
    price = fake.pyfloat(left_digits=2, right_digits=2, positive=True)
    ingredients = fake.words(3)
    vegetarian = fake.pybool()
    sauce = fake.word()

    return {
        "id": fake.random_int(min=1, max=100),
        "name": pizza_name,
        "pizza": pizza_name,
        "price": price,
        "ingredients": ingredients,
        "vegetarian": vegetarian,
        "sauce": sauce
    }

message = generate_fake_pizza()
print(json.dumps(message))