from MiniBlockchain.src.KeyPair import PublicKey, PrivateKey
from MiniBlockchain.src.Signature import Signature

pub_key_path = './keys/public.pem'
private_key_path = './keys/private.pem'
private = PrivateKey()
privateKey = private()

pub = PublicKey()
publicKey = pub()

sign = Signature(pub_key_path, private_key_path)
sign.verifySignature()
sign.signData('New Transaction')
sign.printSignature()
