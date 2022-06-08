from sha1 import sha1_encrypt
import hashlib

ho = hashlib.sha1(b'Hello, world')
h1 = ho.hexdigest()
h2 = sha1_encrypt('Hello, world')[0]
print(h1, h2, h1 == h2)
