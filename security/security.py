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
import json

def random_uuid():
     return uuid.UUID(bytes=bytes(random.getrandbits(8) for _ in range(16)), version=4)


def init_salt(username):
    random.seed(username)
    salt = random_uuid()
    return salt

def create_key(username, password):
    
  
    # Encoding the username and password to utf-8 from unicode (converts a string to bytes). 
    usernameInBytes = username.encode("utf8")
    pwdInBytes = password.encode("utf8")

    '''
    Initialising the key derivation function. This function uses the SHA256 algorithm, the salt generated above and runs the algorithm for
    100 iterations. The length here is the desired length of the derived key in bytes.
    '''

    kdf = pbkdf2_hmac(algorithm=hashes.SHA256(),length=32,salt=salt.bytes,iterations=100,backend=default_backend())

    # Making a key with username and password.
    key=base64.urlsafe_b64encode(kdf.derive(usernameInBytes + pwdInBytes))
    
    print("Key is " + str(key) + "\n")              #Remove later!!!

    # Getting the actual key with Fernet. The object that is returned can only encrypt and decrypt messages using the key passed to Fernet.
    return Fernet(key)

def encrypt(key):
    with open('./test/test.txt', 'rb') as file:
        file_read = file.read()
    encrypted_data = key.encrypt(file_read)
    with open('./test/test.txt', 'wb') as file:
        file.write(encrypted_data)

def parse(text):
    try:
        #return json.loads(text)
        return True
    except ValueError as e:
        print('invalid json: %s' % e)
        return False # or: raise

def decrypt(key):
    with open('./test/test.txt', 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = key.decrypt(encrypted_data)
    # with open('./test/test.txt', 'wb') as file:
    #     file.write(decrypted_data)
    bool_check = parse(decrypted_data)
    if (bool_check == False):
        print("Username or password is incorrect. Please try again.")        
        return False
    with open('./test/test.txt', 'wb') as file:
        file.write(decrypted_data)
    return True

username = input("Please enter your username\n")
password = getpass.getpass()
print("Password is - " + password)
salt = init_salt(username)
key = create_key(username, password)
#encrypt(key)
decrypt(key)

# # If the platform is linux or Mac-OS
# if sys.platform.startswith("linux") or sys.platform.startswith("darwin"):
#     os.system("mkdir " + str(salt))

#     os.system("cd " + str(salt))

#     os.system("ls")


#     #salt = "ac474397d0ae491d952ca3fef63a2444"
#     #salt = binascii.unhexlify(salt)
#     #salt = os.urandom(16)
#     #print(salt)
#     #salt = str(salt)
#     #salt.replace('-',' ')
#     #random = salt.split('-')
#     #salt = "".join(random)
#     #print(salt)
#     #salt = salt.encode()

#     with open('./test/test.txt', 'rb') as file:
#         file_read = file.read()
#     encrypted_data = key.encrypt(file_read)

#     with open('./test/test.txt', 'wb') as file:
#         file.write(encrypted_data)
#     print("Encryption complete. \n")
#     os.system("cat ./test/test.txt")

#     decrypted_data = key.decrypt(encrypted_data)

#     with open('./test/test.txt', 'wb') as file:
#         file.write(decrypted_data)

#     print("\nDecryption done. \n")

#     os.system("cat ./test/test.txt")

# # If the platform is windows
# elif sys.platform.startswith("win32"):
    
#     os.system("mkdir " + str(salt))

#     os.system("cd " + str(salt))

#     os.system("dir")


#     #salt = "ac474397d0ae491d952ca3fef63a2444"
#     #salt = binascii.unhexlify(salt)
#     #salt = os.urandom(16)
#     #print(salt)
#     #salt = str(salt)
#     #salt.replace('-',' ')
#     #random = salt.split('-')
#     #salt = "".join(random)
#     #print(salt)
#     #salt = salt.encode()
    
#     with open('./test/test.txt', 'rb') as file:
#         file_read = file.read()
#     encrypted_data = key.encrypt(file_read)

#     with open('./test/test.txt', 'wb') as file:
#         file.write(encrypted_data)
#     print("Encryption complete. \n")
    
#     os.system("type ./test/test.txt")

#     decrypted_data = key.decrypt(encrypted_data)

#     with open('./test/test.txt', 'wb') as file:
#         file.write(decrypted_data)

#     print("\nDecryption done. \n")

#     os.system("type ./test/test.txt")   
