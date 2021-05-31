import getpass
import os,binascii
import sys
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


def create_key(username, password):
    
    '''
    Initialising the key derivation function. This function uses the SHA256 algorithm, the salt generated above and runs the algorithm for
    100 iterations. The length here is the desired length of the derived key in bytes.
    '''
    kdf = pbkdf2_hmac(algorithm=hashes.SHA256(),length=32,salt=salt.bytes,iterations=100,backend=default_backend())

    # Making a key with username and password.
    key=base64.urlsafe_b64encode(kdf.derive(username + password))
    
    print("Key is " + str(key) + "\n")

    # Getting the actual key with Fernet. The object that is returned can only encrypt and decrypt messages using the key passed to Fernet.
    return Fernet(key)



user = input("Please enter your username\n")
password = getpass.getpass()
print("Password is - " + password)

random.seed(user)

salt = random_uuid()

# Encoding the username and password to utf-8 from unicode (converts a string to bytes). 
user1 = user.encode("utf8")
pwd1 = password.encode("utf8")

f = create_key(user1, pwd1)

# If the platform is linux or Mac-OS
if sys.platform.startswith("linux") or sys.platform.startswith("darwin"):
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

    with open('./test/test.txt', 'rb') as file:
        file_read = file.read()
    encrypted_data = f.encrypt(file_read)

    with open('./test/test.txt', 'wb') as file:
        file.write(encrypted_data)
    print("Encryption complete. \n")
    os.system("cat ./test/test.txt")

    decrypted_data = f.decrypt(encrypted_data)

    with open('./test/test.txt', 'wb') as file:
        file.write(decrypted_data)

    print("\nDecryption done. \n")

    os.system("cat ./test/test.txt")

# If the platform is windows
elif sys.platform.startswith("win32"):
    
    os.system("mkdir " + str(salt))

    os.system("cd " + str(salt))

    os.system("dir")


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
    
    with open('./test/test.txt', 'rb') as file:
        file_read = file.read()
    encrypted_data = f.encrypt(file_read)

    with open('./test/test.txt', 'wb') as file:
        file.write(encrypted_data)
    print("Encryption complete. \n")
    
    os.system("type ./test/test.txt")

    decrypted_data = f.decrypt(encrypted_data)

    with open('./test/test.txt', 'wb') as file:
        file.write(decrypted_data)

    print("\nDecryption done. \n")

    os.system("type ./test/test.txt")   
