
import json
import requests
import settings


def get_my_posts():

    token = settings.get_my_key()

    url = f'https://api.telegram.org/bot{token}/getUpdates'

    my_posts = requests.post(url).json()

    status = my_posts["result"][-1]["message"]["text"]

    return status


if __name__ == "__main__":
    get_my_posts()
