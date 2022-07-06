from KeyPair import KeyPair, PrivateKey, PublicKey
from Singature import Signature
import json
import os
from hashlib import sha256


class Account(KeyPair):

    def __init__(self, account_id: str, wallet: list, balance: int):
        assert account_id[:2] == '1f'
        self.account_id = account_id
        self.wallet = []
        for w in wallet:
            if type(w[0]) == PublicKey and type(w[1]) == PrivateKey:
                self.wallet.append(w)
        if len(self.wallet) == 0:
            for w in wallet:
                if type(w[0]) == str and type(w[1]) == str:
                    super().__init__(w[1], w[0])
                    self.wallet.append([self.publicKey, self.privateKey])
        self.balance = balance

    @staticmethod
    def genAccount() -> object:
        key_pair = KeyPair.genKeyPair()
        acc_id = '1f' + sha256(key_pair.publicKey.key).hexdigest()
        balance = 0
        # _file_input(acc_id, [[key_pair.publicKey.key.hex(), key_pair.privateKey.key.hex()]], balance)
        return Account(acc_id, [[key_pair.publicKey, key_pair.privateKey]], balance)

    def addKeyPairToWallet(self, public_key: bytes, private_key: bytes) -> None:
        super().__init__(public_key, private_key)
        self.wallet.append([self.publicKey, self.privateKey])
        # _file_input(self.account_id, self.wallet, self.balance)

    def updateBalance(self, balance: int) -> None:
        self.balance += balance
        # _file_input(self.account_id, self.wallet, self.balance)

    def getBalance(self) -> int:
        return self.balance

    def printBalance(self) -> None:
        print('Current Balance: ', self.balance, ' coins')

    def signData(self, wallet: list, message: str) -> str:
        sign_object = Signature()
        sign = sign_object.signData(wallet[1], message)
        return sign

    def toString(self) -> str:
        return self.account_id

    def print(self) -> None:
        print('Wallet keys: ')
        for wal in self.wallet:
            print('Private key:', wal[1].key.hex())
            print('Public key: ', wal[0].key.hex())
