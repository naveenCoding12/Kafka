from faker import Faker
import json
from confluent_kafka import SerializingProducer
import logging

logging.basicConfig(level=logging.DEBUG)

# Define a function to serialize the message to be sent to the Kafka topic
def json_serializer(msg, s_obj):
    return json.dumps(msg).encode('ascii')

# Define the configuration for the Kafka producer and create the producer object   
conf = {
    'bootstrap.servers':"kafka-demo-demosygenity-fe98.h.aivencloud.com:26596",
    'client.id': 'avnadmin',
    'security.protocol': 'SSL',
    'ssl.ca.location': './ca.pem',
    'ssl.certificate.location': './service.cert',
    'ssl.key.location': './service.key', 
    'value.serializer': json_serializer,
    'key.serializer': json_serializer
}

producer = SerializingProducer(conf)

# Define a function to generate random messages and produce them to the Kafka topic
def generate_and_produce_fake_pizza(num_producers):
    for _ in range(num_producers):
        message = generate_fake_pizza()
        key = {"id": message["id"]}
        value = message
        producer.produce(
            "pizzas",
            key=key,
            value=value
        )
    producer.flush() 

# Define a function to generate a fake pizza
def generate_fake_pizza():
    fake = Faker()
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

# Generate and produce 10 random messages to the Kafka topic
generate_and_produce_fake_pizza(10)