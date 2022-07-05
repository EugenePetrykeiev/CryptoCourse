from ecdsa import VerifyingKey, SigningKey, BadSignatureError
from hashlib import sha256


class Signature:
    private_key = None
    public_key = None
    message = None
    signature = None

    def __init__(self, pub_key: str, sec_key: str):
        self.public_key = pub_key
        self.private_key = sec_key

    def _get_keys_objects(self) -> tuple:
        vk = VerifyingKey.from_pem(open(self.public_key).read())
        sk = SigningKey.from_pem(open(self.private_key).read())
        return sk, vk

    def _serialized_hash(self, message: str) -> bytes:
        return bytes(sha256(message.encode('utf-8')).digest())

    def verifySignature(self, message: str = "1234567890") -> bool:
        sk, vk = self._get_keys_objects()
        hash_message = self._serialized_hash(message)
        sig = sk.sign(hash_message)
        try:
            vk.verify(sig, hash_message)
            print("good signature")
            return True
        except BadSignatureError:
            print("BAD SIGNATURE")
            return False

    def signData(self, msg: str):
        sk, vk = self._get_keys_objects()
        hash_message = self._serialized_hash(msg)
        sig = sk.sign(hash_message)
        with open("../signature", "wb") as f:
            f.write(sig)
        try:
            vk.verify(sig, hash_message)
            self.signature = sig.hex()
            return sig
        except BadSignatureError:
            raise 'Bad Signature'

    def printSignature(self):
        print(self.signature)
