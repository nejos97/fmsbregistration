import random
import string

def get_random_string():
    letters = string.ascii_lowercase+string.digits
    result_str = ''.join(random.choice(letters) for i in range(10))
    return result_str.upper()