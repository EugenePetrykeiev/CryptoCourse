from sha1 import sha1_encrypt
import hashlib

if __name__ == '__main__':
    ho = hashlib.sha1(b'The quick brown fox jumps over the lazy dog')
    h1 = ho.hexdigest()
    h2 = sha1_encrypt('The quick brown fox jumps over the lazy dog')[0]
    print(h1)
    print(h2)
    print(h1 == h2)
