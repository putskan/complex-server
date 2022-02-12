import random
import uuid


def random_slug():
    return uuid.uuid4().hex.upper()[0 : random.randint(10, 22)]  # noqa
