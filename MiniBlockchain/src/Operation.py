from Singature import Signature


class Operation:
    def __init__(self, sender, receiver, amount: int, sign: bytes):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.sign = sign

    @staticmethod
    def createOperation(sender: object, receiver: object, amount: int, sign: bytes) -> object:
        return Operation(sender, receiver, amount, sign)

    def verifyOperation(self) -> bool:
        sender_balance = self.sender.getBalance()
        if self.amount <= sender_balance:
            sign_object = Signature()
            sign_verify = sign_object.verifySignature(self.sender.wallet[0], self.sign, str(self.amount))
            if sign_verify:
                return True
            else:
                return False
        else:
            return False
