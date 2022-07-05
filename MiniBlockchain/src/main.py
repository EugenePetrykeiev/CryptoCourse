from KeyPair import *
from Singature import Signature

key2 = KeyPair(b'q=\xeaV\xb1\xd3\x9b\xc9\xb3\xbe!O\xc8\x9d\x19b\x0e\xa5\x17[\x83\xb2J\xac\xfc\x0c\xf9~\xb2\xedO\x11',
              b'\xb2\xe1\xf6\x1f)\xab\xd4\x93wB\x81\xe5\x15\xc9\x8b\xc8\x9c\\\xaf\xd9I\xd5\xa42AGFY\x1c#\x8cL\xa5\xa8K\x88\xac\x8c\x987\xfb\t\xb7\xf9\xbd>\xf3\xf1\xf5\x1aAjo\xd0N\x99P\xbc\xf2F:<b2')
# key2 = KeyPair.genKeyPair()
# print(key.privateKey.key)
# print(key.publicKey.key)
# print(key2.privateKey.key)
# print(key2.publicKey.key)
sign = Signature()
signature = sign.signData(key2.privateKey, 'abc')


status=sign.verifySignature(key2.publicKey,signature,'abc')
sign.printSignature()