from Operation import Operation
from Transaction import Transaction
from Block import Block
amount = 15
blocks = []


def block_generator(sender, receiver, block_pool: int, prev_hash: str):
    for i in range(block_pool):
        sender2, amount2, wallet2 = sender.createPaymentOp(receiver, amount, 0)
        message_to_sign = sender.accountID + str(amount)
        signature2 = sender.signData(wallet2, message_to_sign)
        sender3, amount3, wallet3 = sender.createPaymentOp(receiver, amount, 0)
        message_to_sign2 = sender.accountID + str(amount)
        signature3 = sender.signData(wallet3, message_to_sign2)

        op = Operation.createOperation(sender, receiver, amount, signature2)
        op2 = Operation.createOperation(sender, receiver, amount, signature3)

        trx = Transaction.createOperation([op], i)
        trx.printKeyPair()
        trx2 = Transaction.createOperation([op2], i)
        block = Block.createBlock([trx,trx2], prev_hash)
        block.printKeyPair()
        blocks.append(block)
    return blocks
