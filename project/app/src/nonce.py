from base64 import b64encode
from os import urandom

# modified from https://stackoverflow.com/questions/5590170/what-is-the-standard-method-for-generating-a-nonce-in-python
def nonce(length):
    return ''.join(list(filter(lambda s: s.isalpha(), str(b64encode(urandom(length * 2))))))
