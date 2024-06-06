import random
import string


def generate_secret_key(length=30):
    characters = string.ascii_letters + string.digits + string.punctuation
    secret_key = "".join(random.choice(characters) for _ in range(length))
    return secret_key


secret_key = generate_secret_key()
print(f"Generated Secret Key: {secret_key}")
