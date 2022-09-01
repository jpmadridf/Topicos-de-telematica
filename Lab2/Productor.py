import pika
import random

connection = pika.BlockingConnection(pika.ConnectionParameters('23.23.151.188', 5672, '/',
pika.PlainCredentials('user', 'password')))
channel = connection.channel()

channel.basic_publish(exchange="my_exchange", routing_key='test', body=str(random.randint(65,85)))

connection.close()