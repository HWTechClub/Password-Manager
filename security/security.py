import getpass
import os,binascii
import uuid
import random
import string
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC as pbkdf2_hmac
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
#from backports.pbkdf2 import pbkdf2_hmac
from cryptography.fernet import Fernet
import base64

def random_uuid():
     return uuid.UUID(bytes=bytes(random.getrandbits(8) for _ in range(16)), version=4)

user = input("Please enter your username\n")
password = getpass.getpass()
print("Password is - " + password)

random.seed(user)

salt = random_uuid()

os.system("mkdir " + str(salt))

os.system("cd " + str(salt))

os.system("ls")


#salt = "ac474397d0ae491d952ca3fef63a2444"
#salt = binascii.unhexlify(salt)
#salt = os.urandom(16)
#print(salt)
#salt = str(salt)
#salt.replace('-',' ')
#random = salt.split('-')
#salt = "".join(random)
#print(salt)
#salt = salt.encode()
user1 = user.encode("utf8")
pwd1 = password.encode("utf8")
kdf = pbkdf2_hmac(algorithm=hashes.SHA256(),length=32,salt=salt.bytes,iterations=100,backend=default_backend())
key=base64.urlsafe_b64encode(kdf.derive(user1 + pwd1))
print(str(key) + "\n")
f = Fernet(key)


with open('./test/test.txt', 'rb') as file:
    file_read = file.read()
encrypted_data = f.encrypt(file_read)

with open('./test/test.txt', 'wb') as file:
    file.write(encrypted_data)
print("Emcyption complete. \n")
os.system("cat ./test/test.txt")

decrypted_data = f.decrypt(encrypted_data)

with open('./test/test.txt', 'wb') as file:
    file.write(decrypted_data)

print("\nDecryption done. \n")

os.system("cat ./test/test.txt")
