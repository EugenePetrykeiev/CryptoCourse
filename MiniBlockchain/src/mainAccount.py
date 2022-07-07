from Account import Account
from Operation import Operation
from Transaction import Transaction

idx = '1fcaf7e7e27c3f8c48df809a49f0673fb1b37ad5881ee7300ff26970e1d7138532'
wal = [
    "9522f8a224038d32b0c187410f07cc41dcaae2ce184838b06c15ea08f36f214d9f260fc05300087527fe312c9d2bfa79114364626d8fa7c309390a5ad0c4a783",
    "2c26218f21298926d635563f64c4dae57d87630101c5e2e0abe0a7079f354c75"
]
amount = 10

obj = Account(idx, [wal], 0)
obj2 = Account.genAccount()
obj3 = Account.genAccount()
# print(obj.wallet[0][1].key.hex())
obj.addKeyPairToWallet(obj.wallet[0][0].key.hex(), obj.wallet[0][1].key.hex())

obj3.addKeyPairToWallet(wal[0], wal[1])
obj3.updateBalance(100)

wallet = obj3.wallet[0]
sender, amount, wallet = obj3.createPaymentOp(obj, amount, wallet)
obj3.printBalance()
obj.printBalance()

message_to_sign = str(amount)
signature = obj3.signData(wallet, message_to_sign)

obj2.updateBalance(100)
wallet2 = obj2.wallet[0]
sender2, amount2, wallet2 = obj2.createPaymentOp(obj, amount, wallet2)
message_to_sign2 = str(amount)
signature2 = obj2.signData(wallet2, message_to_sign2)

op = Operation.createOperation(obj3, obj, amount, signature)
op2 = Operation.createOperation(obj2, obj, amount2, signature2)
print(op.verifyOperation())
print(op2.verifyOperation())

trx = Transaction.createOperation([op, op2], 2)
trx.printKeyPair()
