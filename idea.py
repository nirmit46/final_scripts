from cryptography.fernet import Fernet
import os
from cryptography.hazmat.primitives.ciphers import Cipher,algorithms, base, modes
from Crypto.Random import get_random_bytes
def IDEA():
    key=os.urandom(16)
    iv=os.urandom(8)
    with open('k3.key', 'wb') as filekey3:
        filekey3.write(key)
    with open('iv.key', 'wb') as i_v:
        i_v.write(iv)

    with open('k3.key', 'rb') as filekey3:
        k3 = filekey3.read()

    with open('iv.key', 'rb') as ivv:
        iv = ivv.read()

    with open('Hello.txt', 'rb') as encrypted_file:
        content = encrypted_file.read()
        b= len(content)
        if(b%8!=0):
            while(b%8!=0):
                content+=" ".encode()
                b=len(content)
    cipher = Cipher(algorithms.IDEA(k3), modes.CFB(iv))
    encryptor = cipher.encryptor()
    en3 = encryptor.update(content) + encryptor.finalize()
    # print(en3)
    decryptor = cipher.decryptor()
    de3 = decryptor.update(en3) +decryptor.finalize()
    return de3

print(IDEA())