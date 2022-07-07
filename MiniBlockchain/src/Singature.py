from KeyPair import PrivateKey, PublicKey
from ecdsa import VerifyingKey, SigningKey, BadSignatureError, SECP256k1
from hashlib import sha256


class Signature:
    def signData(self, private_key: PrivateKey, message: str) -> bytes:
        sk = SigningKey.from_string(private_key.key, curve=SECP256k1, hashfunc=sha256)
        message = message.encode('utf-8')
        self._sign = sk.sign(message)
        return self._sign

    def verifySignature(self, public_key: PublicKey, sign: bytes, message: str) -> bool:
        vk = VerifyingKey.from_string(public_key.key, curve=SECP256k1, hashfunc=sha256)
        message = message.encode('utf-8')
        try:
            self.result = vk.verify(sign, message)  # True
        except BadSignatureError:
            return False
        return self.result

    def printSignature(self) -> None:
        print('Signature bytes: ', self._sign)
        print('Signature hex: ', self._sign.hex())
        print('Verification status: ', self.result)

    def toString(self) -> str:
        return self._sign.hex()
