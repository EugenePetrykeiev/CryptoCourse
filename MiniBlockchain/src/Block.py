class Block:
    def __init__(self, block_id: str, prev_hash: str, trx_list: list):
        self.blockID = block_id
        self.prevHash = prev_hash
        self.setOfTransactions = trx_list

    @staticmethod
    def createBlock(trx_list: list, prevHash: str) -> object:
        from Hash import Hash
        block_id = ''
        for trx in trx_list:
            block_id += trx.transactionID + str(trx.nonce)
        block_id = Hash.toSHA1(block_id)
        return Block(block_id, prevHash, trx_list)

    def printKeyPair(self) -> None:
        for trx in self.setOfTransactions:
            for idx, op in enumerate(trx.setOfOperations):
                print('Transaction index: ', idx)
                print('**Sender information**')
                print('Sender Wallet Public Key:', op.sender.wallet[0][0].key.hex())
                print('Sender Wallet Private Key:', op.sender.wallet[0][1].key.hex())
                print('Sender Account Balance:', op.sender.getBalance())
                print('**Receiver information**')
                for keys in op.receiver.wallet:
                    print('Receiver Wallet Public Key: ', keys[0].key.hex())
                    print('Receiver Wallet Private Key: ', keys[1].key.hex())
                    print('Receiver Account Balance:', op.receiver.getBalance())
                    print('-----')
            print('Transaction hash ID: ', trx.transactionID)
            print('')
        print('Block hash id: ', self.blockID, '\n')
        print('-----End of block-----')

    def toString(self) -> str:
        return self.blockID
