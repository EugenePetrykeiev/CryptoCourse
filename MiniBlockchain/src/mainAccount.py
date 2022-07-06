from Account import Account
import json

idx = '1fcaf7e7e27c3f8c48df809a49f0673fb1b37ad5881ee7300ff26970e1d7138532'
wal = [
    "9522f8a224038d32b0c187410f07cc41dcaae2ce184838b06c15ea08f36f214d9f260fc05300087527fe312c9d2bfa79114364626d8fa7c309390a5ad0c4a783",
    "2c26218f21298926d635563f64c4dae57d87630101c5e2e0abe0a7079f354c75"
]
# obj = Account(idx,[wal],0)
# obj2=Account.genAccount()
obj3 = Account.genAccount()
obj3.addKeyPairToWallet(wal[0], wal[1])
obj3.updateBalance(100)
obj3.printBalance()
wallet=obj3.wallet[0]
print(obj3.publicKey.key.hex())
print(obj3.privateKey.key.hex())
obj3.signData(wallet,'Hello, world!')
obj3.print()
# print(obj3.wallet[1][0].key.hex())

# key_id1 = '1f114b6a0de9efad7c06b73f1c40bf6d21012a66539dca472fb2113d274fba8204'
# key_id2 = '1fcaf7e7e27c3f8c48df809a49f0673fb1b37ad5881ee7300ff26970e1d7138532'
#
#
# # acc1 = Account.genAccount()
# def open_account(key_id):
#     with open('accounts.json', 'r') as f:
#         data = json.loads(f.read())
#     f.close()
#     index = ['Key' if i['AccountID'] == key_id else None for index, i in enumerate(data)].index('Key')
#     acc_obj = Account(data[index]['AccountID'], data[index]['Wallet'], data[index]['Balance'])
#     return acc_obj
#
#
# main_account = open_account(key_id2)
# second_account = open_account(key_id1)
# print(main_account.balance)
# main_account.createPaymentOp(second_account,15,main_account.wallet[0])
# main_account.printBalance()

# main_account.updateBalance(140)
# second_account.updateBalance(1000)
