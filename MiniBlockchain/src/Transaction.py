from hashlib import sha256


class Transaction:
    def __init__(self, txid: str, op_list: list, nonce: int):
        self.transactionID = txid
        self.setOfOperations = op_list
        self.nonce = nonce

    @staticmethod
    def createOperation(op_list: list, nonce: int) -> object:
        trxs_id = ''
        for op in op_list:
            temp = sha256(
                bytes.fromhex(
                    op.sender.accountID +
                    op.receiver.accountID
                ) +
                op.sign +
                nonce.to_bytes(2, 'big') +
                op.amount.to_bytes(2, 'big')
            ).hexdigest()
            trxs_id += temp
        trxs_id = sha256(bytes.fromhex(trxs_id)).hexdigest()
        return Transaction(trxs_id, op_list, nonce)

    def toString(self):
        return self.transactionID

    def printKeyPair(self):
        for idx, op in enumerate(self.setOfOperations):
            print('Transaction index: ', idx)
            print('**Sender information**')
            print('Sender Wallet Public Key:', op.sender.wallet[0].key.hex())
            print('Sender Wallet Private Key:', op.sender.wallet[1].key.hex())
            print('**Receiver Infromation**')
            print('Receiver Wallet Public Key: ', op.receiver.wallet[0][0].key.hex())
            print('Receiver Wallet Private Key: ', op.receiver.wallet[0][1].key.hex())
            print('')
        print('Transaction hash ID: ', self.transactionID)
