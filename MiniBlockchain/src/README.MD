
#KeyPair class
Класс для генерации публичного и приватного ключей при помощи алгоритма ECDSA 
с использованием эллиптической кривой _SECP256k1_.
Дополнительные классы PublicKey и PrivatKey возращают ключи формата HEX и генерируют пару ключей в стандартизированных файлах
PEM формата.

###Пример использования:
````python
from MiniBlockchain.src.KeyPair import PublicKey, PrivateKey

private = PrivateKey()
privateKey = private()

pub = PublicKey()
publicKey = pub()
````
Ключи генерируются также в файлах:
```
./keys/private.pem
./keys/public.pem
```

Если эти файлы созданы, то данные используются непосредственно из текущих файлов. Новая пара ключей выдается
автоматически, если этих файлов не существует.

Класс KeyPair также дополнительно имеет методы:
- genKeyPair
- printKeyPair

#Signature class
Класс предназначен для верификации пары ключей при помощи создания тестового сообщения и его подписи
с дальнейшим расшифрованием и подтверждением верификации пары ключей.

Метод ожидает путь к стандартизированным файлам PEM

###Пример использования:

````python
from MiniBlockchain.src.Signature import Signature
pub_key_path = './keys/public.pem'
private_key_path = './keys/private.pem'
sign = Signature(pub_key_path, private_key_path)
sign.verifySignature()
sign.signData('New Transaction')
sign.printSignature()
````
Методы, класса:
- signData( message )
- verifySignature()