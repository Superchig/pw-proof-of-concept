import random, string

def gen_password():
    """
    Simple function to generate a random 10-character password.
    Taken from Wikipedia.
    """
    myrg = random.SystemRandom()
    length = 10
    alphabet = string.ascii_letters + string.digits
    pw = str().join(myrg.choice(alphabet) for _ in range(length))
    return pw
