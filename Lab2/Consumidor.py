from base64 import decode
from gc import callbacks
import pika
import time
import requests

TOKEN = "BBFF-n28miwzro80gtItx8hI9EddFLqWzvo"  # Put your TOKEN here
DEVICE_LABEL = "lab2"  # Put your device label here 
VARIABLE_LABEL_1 = "humidity"  # Put your first variable label here


def callback(ch, method, properties,body):
    # Creates two random values for sending data
    value_1 = body.decode('UTF-8')
    payload = {VARIABLE_LABEL_1:value_1}
    post_request(payload)


def post_request(payload):
    # Creates the headers for the HTTP requests
    url = "http://industrial.api.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

    # Makes the HTTP requests
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.post(url=url, headers=headers, json=payload)
        status = req.status_code
        attempts += 1
        time.sleep(1)

    # Processes results
    print(req.status_code, req.json())
    if status >= 400:
        print("[ERROR] Could not send data after 5 attempts, please check \
            your token credentials and internet connection")
        return False

    print("[INFO] request made properly, your device is updated")
    return True


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('23.23.151.188', 5672, '/',
    pika.PlainCredentials('user', 'password')))
    channel = connection.channel()
    channel.basic_consume(queue="my_app", on_message_callback=callback, auto_ack=True)
    channel.start_consuming()


if __name__ == '__main__':
    while (True):
        main()
        time.sleep(1)