from Blockchain import Blockchain, Account
from NewBockGen import block_generator
import json

sender = Account.genAccount()
sender.updateBalance(100)
receiver = Account.genAccount()

bc = Blockchain.initBlockchain()
blocks = block_generator(sender, receiver, 2, bc.blockHistory[0].blockID)
print('Initial database', bc.coinDatabase)
bc.getTokenFromFaucet(sender, 5)
bc.getTokenFromFaucet(receiver, 90)
receiver.printBalance()
sender.printBalance()

bc.validateBlock(blocks[0])
bc.validateBlock(blocks[1])

print('Transaction history: \n', bc.txDatabase)
print('Block History: \n', bc.blockHistory)
print('Accounts database: \n', json.dumps(bc.coinDatabase, indent=2))
