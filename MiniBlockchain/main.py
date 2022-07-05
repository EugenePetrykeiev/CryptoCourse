from MiniBlockchain.old.KeyPair import PublicKey, PrivateKey
from MiniBlockchain.old.Signature import Signature

pub_key_path = './keys/public.pem'
private_key_path = './keys/private.pem'
private = PrivateKey()
privateKey = private()

pub = PublicKey()
publicKey = pub()

sign = Signature(pub_key_path, private_key_path)
sign.verifySignature()
s = sign.signData('New Transaction')
print(s)
sign.printSignature()
