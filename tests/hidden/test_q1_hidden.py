from q1 import transform_string
import random
import string

def test_random_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(200))
    r = transform_string(s)

    for i, ch in enumerate(s):
        if ch.lower() in "aeiou":
            assert r[i].isupper()
        else:
            assert r[i].islower()
