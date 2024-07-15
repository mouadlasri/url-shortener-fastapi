import string
import random

# util function to generate a random string of specific length
def create_random_key(length: int = 6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))