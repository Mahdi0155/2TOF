import random
from config import FAKE_NAMES
from datetime import datetime, timedelta

def generate_fake_user():
    return {
        'name': random.choice(FAKE_NAMES),
        'gender': random.choice(['male', 'female']),
        'age': random.randint(18, 35),
        'bio': random.choice([
            'I love traveling', 'Music is my life', 'Coder at heart', 
            'Looking for new friends', 'Life is beautiful'
        ])
    }

def get_random_disconnect_time():
    return random.randint(600, 1200)  # 10 تا 20 دقیقه

def chance_disconnect():
    return random.random() < 0.15  # 15 درصد

def message_miss_chance():
    return random.random() < 0.5  # 50 درصد
