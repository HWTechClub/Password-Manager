import uuid
import random
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC as pbkdf2_hmac
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import base64

# Initializes the salt
def init_salt(username):
    random.seed(username)
    return uuid.UUID(bytes=bytes(random.getrandbits(8) for _ in range(16)), version=4)

def create_key(username, password):
    
  
    # Encoding the username and password to utf-8 from unicode (converts a string to bytes). 
    usernameInBytes = username.encode("utf8")
    pwdInBytes = password.encode("utf8")

    # Initializing the salt
    salt = init_salt(username)

    '''
    Initialising the key derivation function. This function uses the SHA256 algorithm, the salt generated above and runs the algorithm for
    100 iterations. The length here is the desired length of the derived key in bytes.
    '''

    kdf = pbkdf2_hmac(algorithm=hashes.SHA256(),length=32,salt=salt.bytes,iterations=100,backend=default_backend())

    # Making a key with username and password.
    key=base64.urlsafe_b64encode(kdf.derive(usernameInBytes + pwdInBytes))
    
    #print("Key is " + str(key) + "\n")              #Remove later!!!

    # Getting the actual key with Fernet. The object that is returned can only encrypt and decrypt messages using the key passed to Fernet.
    return Fernet(key)

def encrypt(key):
    #Stores file contents in file_read.
    with open('../passwords/user.json', 'rb') as file:
        file_read = file.read()
    #Encrypts file_read and writes it into the file.
    encrypted_data = key.encrypt(file_read)
    with open('../passwords/user.json', 'wb') as file:
        file.write(encrypted_data)


def decrypt(key):
    #Reads the file.
    with open('../passwords/user.json', 'rb') as file:
        encrypted_data = file.read()
    #Fernet returns an error if the key for decryption is not the same as the key for encryption.
    try:
        decrypted_data = key.decrypt(encrypted_data)
    except:
        print("Username or password is incorrect. Please try again.")        
        return False
    #Writes decrypted data back to the file.
    with open('../passwords/user.json', 'wb') as file:
        file.write(decrypted_data)
    return True