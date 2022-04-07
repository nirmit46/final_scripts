from cryptography.fernet import Fernet
import os
from cryptography.hazmat.primitives.ciphers import Cipher,algorithms, base, modes
from Crypto.Cipher import DES3


#################################################################################






################################################################################################
# opening the key1
with open('k1.key', 'rb') as filekey1:
    key1 = filekey1.read()
  
# using the generated key
fernet1 = Fernet(key1)

with open("parts/f1.txt",'rb') as part1:
    f1=part1.read()
    part1.close()
#decrpyting the first fragment
de1 = fernet1.decrypt(f1)

################################################################################################
# opening the key2 andd nonce variable
with open('k2.key', 'rb') as filekey2:
    key2 = filekey2.read()

with open('nonce.key','rb') as nonce2:
    nonce = nonce2.read()

with open("parts/f2.txt",'rb') as part2:
    f2=part2.read()
    part2.close()

cipher= DES3.new(key2,DES3.MODE_EAX,nonce=nonce)
de2 = cipher.decrypt(f2)


################################################################################################
# opening the key3
with open('k3.key', 'rb') as filekey3:
    key3 = filekey3.read()

with open('iv.key', 'rb') as ivv:
   iv = ivv.read()


#reading the first line i.e. third fragment

with open("parts/f3.txt",'rb') as part3:
    f3=part3.read()
    part3.close() 

#decrpyting the first fragment
cipher = Cipher(algorithms.IDEA(key3), modes.CFB(iv))
decryptor = cipher.decryptor()
de3 = decryptor.update(f3) +decryptor.finalize()


################################################################################################
  
# opening the file in write mode and writing the decrypted data
with open('Hello.txt', 'wb') as dec_file:
   dec_file.write(de1)
   dec_file.write(de2)
   dec_file.write(de3.strip())
    
    