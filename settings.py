
from dotenv import load_dotenv
import os


def get_my_key():

    load_dotenv()

    telegram_key = os.getenv("TELEGRAM_TOKEN")

    return telegram_key
