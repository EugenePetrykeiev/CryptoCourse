from aes128 import aes_encryption
import base64

cipher = aes_encryption('123456789012345', '1234567890abcdef')
message_bytes = cipher.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')
print('Cipher: ', cipher)
print('Base 64: ', base64_message)
