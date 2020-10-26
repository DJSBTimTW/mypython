from cryptography import Random
from cryptography.Hash import SHA
from cryptography.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from cryptography.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from cryptography.PublicKey import RSA

# 偽隨機數生成器
random_generator = Random.new().read
# rsa演算法生成例項
rsa = RSA.generate(1024, random_generator)

# master的祕鑰對的生成
private_pem = rsa.exportKey()

with open('master-private.pem', 'w') as f:
  f.write(private_pem)

public_pem = rsa.publickey().exportKey()
with open('master-public.pem', 'w') as f:
  f.write(public_pem)

# ghost的祕鑰對的生成
private_pem = rsa.exportKey()
with open('master-private.pem', 'w') as f:
  f.write(private_pem)

public_pem = rsa.publickey().exportKey()
with open('master-public.pem', 'w') as f:
  f.write(public_pem)