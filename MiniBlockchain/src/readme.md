# Blockchain realization

## Содержание классов:

- KeyPair
- Account
- Signature
- Operation
- Transaction
- Hash
- Block
- Blockchain

## Класс KeyPair

Класс реализует генерацию пары ключей: публичного и приватного. Генерация проводится алгоритмом ECDSA. С использованием
кривой _SECP256k1_. Пару ключей можно сгенерировать или же задать вручную в __str__ или __bytes__ формате. Метод __
genKeyPair()__ даёт возможность получить ключи в виде объектов классов PublicKey и PrivateKey для дальнейшего
использования. Метод __printKeyPair()__ - дает возможность вывести на экран значения соотвествующего класса.

### Пример генерации аккаунта

```python
from KeyPair import *
from Singature import Signature

first_account = KeyPair(
    b'\x8b\xd6\xd0\xb8I\x0c\x9bVH\xe5r.\xf9\x9d\xeb2\tk\x89`Uk,\xca\x1f!\xcd(\x7f\xae\xd4\x86\x18\xe0I|Kuh\x1c\x85\x9c \xe8}\xbb\xbc\xf7\x82\x8b,\x16\xacE7n\xe7cD\x8f\xae|\x92\x07',
    b'\x83\xe3\xa8\xd6\x8f\xf8\xd1(\xe9\xc7!\t4\x00M6\x9e\xe0\xb3\xe9\x99f\nx\x1f\xef:S\xf0<\xc5\xaa'
)

second_account = KeyPair.genKeyPair()

pub_k = first_account.publicKey
private_k = first_account.privateKey
sign_acc_1 = Signature()
sign1 = sign_acc_1.signData(private_k, 'abc')
sign_acc_1.verifySignature(pub_k, sign1, 'abc')
sign_acc_1.printSignature()
first_account.printKeyPair()

print('\n\n\n\n')

pub_k = second_account.publicKey
private_k = second_account.privateKey
sign_acc_2 = Signature()
sign2 = sign_acc_2.signData(private_k, 'abc')
sign_acc_2.verifySignature(pub_k, sign2, 'abc')
sign_acc_2.printSignature()
second_account.printKeyPair()


```

Пример позволяет сгенерировать пару ключей и верифицировать их при помощи создания тестовой подписи и её проверки, а
также вручную добавить пару ключей и также их верифицировать.

## Класс Account

Класс позволяет создать аккаунт с использованием собственной пары ключей или же с их автоматической генерацией. Создает
аккаунт с формированием ID аккаунта, где правильным ID является строка - результат конкантинации  ___1f_ + _sha256(
public key)___.

Класс имеет методы:

- `genAccount()` - генерирует аккаунт при помощи класса KeyPair
- `addKeyPairToWallet(public key, private key)` - позволяет добавить в аккаунт собственную пару ключей и использовать её
  для транзакций
- `updateBalance(amount)` - позволяет обновить баланс аккаунта
- `getBalance()` - возвращает значение баланса аккаунта
- `createPaymentOp(receiver, amount, wallet id)` - создает операцию передачи баланса другому аккаунту
- `signData(wallet, message)` - подпись данных выбранным кошельком
- `printBalance()` - печать текущего баланса
- `toString()` - возвращает ID аккаунта
- `print()` - печатает ключевые пары аккаунта

### Пример использования

```python
from Account import Account

idx = '1f' + ''.zfill(64)

wal = [
    "2c26218f21298926d635563f64c4dae57d87630101c5e2e0abe0a7079f354c75",
    "9522f8a224038d32b0c187410f07cc41dcaae2ce184838b06c15ea08f36f214d9f\
    60fc05300087527fe312c9d2bfa79114364626d8fa7c309390a5ad0c4a783",

]
amount = 10

sender = Account(idx, [wal], 0)
receiver = Account.genAccount()

receiver, amount, wallet = sender.createPaymentOp(receiver, amount, 0)
message_to_sign = sender.accountID + str(amount)
signature2 = sender.signData(wallet, message_to_sign)
```

Создание аккаунта отправителя и получателя, с созданием операции передачи баланса аккаунту-получателю. Генерация подписи
на данную операцию в байтах.

## Класс Operation

Класс Operation создает операцию и верифицирует её для передачи в будущую транзакцию. Одна транзакция может содержать
несколько операций.

Метод __verifyOperation()__ - проверяет созданную операцию при помощи класса _createOperation()_ и возвращает True или
False.

### Пример использования

```python
from Operation import Operation

op = Operation.createOperation(sender, receiver, amount, signature)
print(op.verifyOperation())
op.printKeyPair()
```

```
True
Sender Wallet [[<KeyPair.PublicKey object at 0x000002437C3A1E50>, <KeyPair.PrivateKey object at 0x000002437C3A1EB0>]]
Receiver Wallet [[<KeyPair.PublicKey object at 0x000002437C3A1FD0>, <KeyPair.PrivateKey object at 0x000002437C3A1A30>]]
```

## Класс Transaction

Класс создает транзакцию из списка операций. Формирует id транзакции в виде хеша результата конкантенации:
``
Sender.ID + Receiver.ID + Sign + Nonce + Amount
``

### Пример использования

```python
from Transaction import Transaction

trx = Transaction.createOperation([op], nonce)
trx.printKeyPair()
```

```
**Sender information**
Sender Wallet Public Key: 21d9d3832de9f83db104717e90eb42a99de7c829e4cff29a838cc1e985cd85d33cbb7a70e5530284e0cc4a49ef44dbc3028ac99a4984bd46af59d6fe9bd28f88
Sender Wallet Private Key: c24c7413c4ebb5c5c7900914a7fbb0c48d50ba98b39b657ed4eed701482b9c07
**Receiver information**
Receiver Wallet Public Key:  8502126782f1b8db1cf58d6231ac0792819b0494b792ea5e5db871e987595e8d83a58502e3f9328af88c25a2edac1496f2742c85f7a4a3eda9abaf8ed1ec58d6
Receiver Wallet Private Key:  44838694b2a3ecef0d0c3314e52b397b0448da9fb9c5ff120807c99250562f4c
```

## Класс Block

Класс Block формирует блок из транзакций. Список транзакций подается в
метод `createBlock(transactions list, previous block hash)`, а также хеш заголовка предыдущего блока. Метод возвращает
блок с необходимыми данными.

### Пример использования

```python
from Block import Block

block = Block.createBlock([trx, trx2], prev_hash)
block.printKeyPair()
```

### Пример сформированного блока с транзакциями

```
Transaction index:  0
**Sender information**
Sender Wallet Public Key: 70067bd36e36f000bc61f78943b186df528f58d0b2d48ac8f2723fdda82a8230e1be903d0ccef0f5382953e54f4f679a25560bce0fb1c0855eab28485d9bf711
Sender Wallet Private Key: 7b414749e6f46b138048d99b7da31f8ad09f22bc1fc92f567f3f7c332b94d11c
Sender Account Balance: 100
**Receiver information**
Receiver Wallet Public Key:  a4594749eb7561c0e17d7b0970cb2a206051d699545f55a38ca3b6e7bb101d4d1dc1b17f2da99352f23a85cfed336ec7d7ff3b6d26fce769b09a76cc3513e76c
Receiver Wallet Private Key:  93376cd3b15da3971c2f6360ea8ef5fde91e7c4bbd1577c6e4d401040911de92
Receiver Account Balance: 0
-----
Transaction hash ID:  2aa9186220c5e5716e595fe8aa5bde716b945b58507505172ea20ca67f54cb0a

Block hash id:  57f2d9e61521d3c3559b52817d4cc22c32707bd0 

-----End of block-----

Process finished with exit code 0

```

## Класс Blockchain

Класс формирует генезисный блок и добавляет его в цепочку блоков. Также добавляет созданные блоки в цепочку блоков перед
их проверкой.

Методы:

- `initBlockchain()` - создает генезисный блок на адрес 1f0000.... и добавляет первую транзакцию в блок без проверки,
  формируя хеш этого блока.

- `getTokenFromFaucet(account, amount)` - При инициализации есть монеты, которые можно передать аккаунту с "воздуха".
  Добавляется, в поле coinsDatabase, но не отображается, как транзакция.

- `validateBlock(block)` - принимает блок в качестве аргумента метода. Проверяет целостность цепочки блока, подписи
  каждой транзакции в блоке, повторение id транзакций (для избегания повторяющихся транзакций) и балансы аккаунтов. Если
  результат успешный, то в coinsDatabase обновляется информация об аккаунтах или добавляется новый аккаунт, если он не
  был еще создан. Блок попадает в список истории блоков. Транзакции этого блока попадают в список транзакций для
  быстрого их поиска в будущем.

### Пример использования

```python
from Blockchain import Blockchain, Account
import json

sender = Account.genAccount()
sender.updateBalance(100)
receiver = Account.genAccount()

bc = Blockchain.initBlockchain()
print('Initial database', bc.coinDatabase)
bc.getTokenFromFaucet(sender, 5)
bc.getTokenFromFaucet(receiver, 90)
receiver.printBalance()
sender.printBalance()

print('Transaction history: \n', bc.txDatabase)
print('Block History: \n', bc.blockHistory)
print('Accounts database: \n', json.dumps(bc.coinDatabase, indent=2))
```

Добавим для двух существующих аккаунтов монеты из крана блокчейна. В результате coinDatabase хранит в себе три аккаунта
с балансами, а блок всего один - генезис блок.

```
Initial database [{'ID': '1f0000000000000000000000000000000000000000000000000000000000000000', 'Balance': 10}]
Current Balance:  90  coins
Current Balance:  105  coins
Transaction history: 
 [<Transaction.Transaction object at 0x000002EFFEB41B80>]
Block History: 
 [<Block.Block object at 0x000002EFFEB41CD0>]
Accounts database: 
 [
  {
    "ID": "1f0000000000000000000000000000000000000000000000000000000000000000",
    "Balance": 10
  },
  {
    "ID": "1f9d93e9a27a85b58ec2878df422d73d6749929d490475b89dbb36840cd8ce1334",
    "Balance": 105
  },
  {
    "ID": "1f85ab72c36d749495cfa4fb0c78ef7e0c7ed70dade060e1b391688a3c5996d352",
    "Balance": 90
  }
]
```

### Генератор блоков для проверки

Файл **NewBockGen** позволяет использовать метод `block_generator(sender, receiver, iters, start block hash)`
который возвращает массив непроверенных блоков, которые повторяют одни и те же транзакции, но имеют разные подписи и
разные **tx_id**. Пример использования

```python
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
```

### Полученные результаты:

```
Initial database [{'ID': '1f0000000000000000000000000000000000000000000000000000000000000000', 'Balance': 10}]
Current Balance:  90  coins
Current Balance:  105  coins
Transaction history: 
 [<Transaction.Transaction object at 0x0000015A5F8251F0>, <Transaction.Transaction object at 0x0000015A5F8257F0>, <Transaction.Transaction object at 0x0000015A5F825700>, <Transaction.Transaction object at 0x0000015A5F8259D0>, <Transaction.Transaction object at 0x0000015A5F825880>]
Block History: 
 [<Block.Block object at 0x0000015A5F8252E0>, <Block.Block object at 0x0000015A5F825610>, <Block.Block object at 0x0000015A5F825850>]
Accounts database: 
 [
  {
    "ID": "1f0000000000000000000000000000000000000000000000000000000000000000",
    "Balance": 10
  },
  {
    "ID": "1f63ad0eb8f4e7f5bfbae949568f4fa880064ce5b11b87b348f4c6cc32371845fe",
    "Balance": 45
  },
  {
    "ID": "1f32a369395bb9eb86d0879f633e7c4a94c0e2bd960fb557f271dee0b4445522dc",
    "Balance": 150
  }
]
```

## Дополнительные классы

### Класс Signature

Клас позволяет создать подпись любых данных при помощи приватного ключа и верифицировать эти данные при помощи
публичного ключа. Возвращает метод **bool** значение.

### Класс Hash

Статический класс с методом `toSHA1(string message)`, который используется для формирование хеша заголовка блоков.

