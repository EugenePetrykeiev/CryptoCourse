from Account import Account
from Operation import Operation
from Transaction import Transaction
from Block import Block


class Blockchain:
    def __init__(self, coins_database: list, block_hist: list, tx_database: list, faucet_coins: int = 100):
        self.coinDatabase = coins_database
        self.blockHistory = block_hist
        self.txDatabase = tx_database
        self.faucetCoins = faucet_coins

    @staticmethod
    def initBlockchain():
        idx = '1f' + ''.zfill(64)
        wal = [
            "2c26218f21298926d635563f64c4dae57d87630101c5e2e0abe0a7079f354c75",
            "9522f8a224038d32b0c187410f07cc41dcaae2ce184838b06c15ea08f36f214d9f260fc05300087527fe312c9d2bfa79114364626d8fa7c309390a5ad0c4a783",
        ]
        amount = 0
        obj = Account(idx, [wal], 10)
        obj.updateBalance(amount)
        sender, amount, wallet = obj.createPaymentOp(obj, amount, 0)
        op = Operation.createOperation(obj, obj, amount, sign=b'00000000')
        trx = Transaction.createOperation([op], nonce=1000001)
        print('Genesis transaction id:', trx.transactionID)
        block = Block.createBlock([trx], '0')
        coins_database = {
            'ID': block.setOfTransactions[0].setOfOperations[0].receiver.accountID,
            'Balance': block.setOfTransactions[0].setOfOperations[0].receiver.getBalance()
        }
        return Blockchain([coins_database], [block], [trx])

    def getTokenFromFaucet(self, account, faucet_amount: int) -> None:
        if faucet_amount <= self.faucetCoins:
            self.faucetCoins -= faucet_amount
            account.updateBalance(faucet_amount)
            state = {
                'ID': account.accountID,
                'Balance': account.getBalance()
            }
            if not any(data['ID'] == state['ID'] for data in self.coinDatabase):
                self.coinDatabase.append(state)
            else:
                for idx, data in enumerate(self.coinDatabase):
                    if data['ID'] == state['ID']:
                        self.coinDatabase[idx] = state
        else:
            print('Rejected!! Operation was skipped')

    def validateBlock(self, block):
        last_block = self.blockHistory[-1].blockID
        if last_block == block.prevHash:
            for tx_id_new in block.setOfTransactions:
                for ops in tx_id_new.setOfOperations:
                    if ops.verifyOperation() and ops.sender.getBalance() >= ops.amount:
                        for tx_id_hist in self.txDatabase:
                            if tx_id_new.transactionID == tx_id_hist.transactionID:
                                return False
        self.blockHistory.append(block)
        for tx_id_new in block.setOfTransactions:
            self.txDatabase.append(tx_id_new)
            for ops in tx_id_new.setOfOperations:
                ops.receiver.updateBalance(ops.amount)
                coins_database = {
                    'ID': ops.receiver.accountID,
                    'Balance': ops.receiver.getBalance()
                }

                if not any(data['ID'] == coins_database['ID'] for data in self.coinDatabase):
                    self.coinDatabase.append(coins_database)
                else:
                    for idx, data in enumerate(self.coinDatabase):
                        if data['ID'] == coins_database['ID']:
                            self.coinDatabase[idx] = coins_database
                ops.sender.updateBalance(-ops.amount)
                coins_database = {
                    'ID': ops.sender.accountID,
                    'Balance': ops.sender.getBalance()
                }
                if not any(data['ID'] == coins_database['ID'] for data in self.coinDatabase):
                    self.coinDatabase.append(coins_database)
                else:
                    for idx, data in enumerate(self.coinDatabase):
                        if data['ID'] == coins_database['ID']:
                            self.coinDatabase[idx] = coins_database
        return True
