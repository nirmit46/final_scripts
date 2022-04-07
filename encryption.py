from cryptography.fernet import Fernet
import os
from cryptography.hazmat.primitives.ciphers import Cipher,algorithms, base, modes
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes


with open("parts/f1.txt",'r') as part1:
    f1=part1.read()
    part1.close()
with open("parts/f2.txt",'r') as part2:
    f2=part2.read()
    part2.close()
with open("parts/f3.txt",'r') as part3:
    f3=part3.read()
    part3.close() 


# key1 generation for AES
k1 = Fernet.generate_key()
  
# string the key in a file
with open('k1.key', 'wb') as filekey1:
   filekey1.write(k1)

# opening the key1
with open('k1.key', 'rb') as filekey1:
    k1 = filekey1.read()
  
# using the generated key1
fernet1 = Fernet(k1)

def AES(f1,fernet1):

    x1= bytes(f1, 'utf-8')
    en1 = fernet1.encrypt(x1) 
    # return en1
    with open("parts/f1.txt",'wb') as et1:
        et1.write(en1)







###################################################################
# key2 generation for DES3
while True:
    try:
        k2= DES3.adjust_key_parity(get_random_bytes(24))
        with open('k2.key', 'wb') as filekey2:
            filekey2.write(k2)
        break
    except ValueError:
        pass



def desen(f2,k2):
    x2=bytes(f2,'utf-8')
    cipher = DES3.new(k2, DES3.MODE_EAX)
    nonce = cipher.nonce
    en2 = cipher.encrypt(x2)
    with open('nonce.key', 'wb') as noncevar:
            noncevar.write(nonce)
    with open("parts/f2.txt",'wb') as et2:
        et2.write(en2)
  

  
k3 = os.urandom(16)
# string the key in a file
with open('k3.key', 'wb') as filekey3:
   filekey3.write(k3)

# opening the key1
with open('k3.key', 'rb') as filekey3:
    k3 = filekey3.read()


def IDEA(f3,k3):
    x3=bytes(f3,'utf-8')
    b=len(x3)
    if(b%8!=0):
        while(b%8!=0):
            x3+=" ".encode()
            b=len(x3)
    
    iv = os.urandom(8)
    with open('iv.key', 'wb') as i_v:
            i_v.write(iv)
    cipher = Cipher(algorithms.IDEA(k3), modes.CFB(iv))
    encryptor = cipher.encryptor()
    en3 = encryptor.update(x3) + encryptor.finalize()
    with open("parts/f3.txt",'wb') as et3:
        et3.write(en3)

AES(f1,fernet1)
desen(f2,k2)
IDEA(f3,k3)

open("Hello.txt",'w').close() 
    
# with open('Hello.txt', 'wb') as encrypted_file:

#     encrypted_file.write(AES(f1,fernet1))
#     line = str() + "\n"
#     encrypted_file.write(line.encode('utf-8'))

#     f2=bytes(f2,'utf-8')
#     encrypted_file.write(desen(f2,k2))

#     line = str() + "\n"
#     encrypted_file.write(line.encode('utf-8'))

#     f3=bytes(f3,'utf-8')
    
#     encrypted_file.write(IDEA(f3,k3))
# encrypted_file.close()
 
    