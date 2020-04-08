""" Rivest-Shamir-Adleman Cryptosystem
@author Moses Borore"""
import math
import random
import json

# Finding the two prime numbers
def is_prime(n):
	
	if n == 2:
		return False
	elif n < 2 and n % 2 == 0:
		return False
			
#	max_divisor = math.floor(math.sqrt(n))
	
	for d in range (2, n):
		if n % d == 0:
			return False
	return True

# store all primes numbers in a list
primes = [i for i in range(1, 101) if is_prime(i)]

#print(primes)

def rand_prime():
	return random.choice(primes)

# 1st prime number
p = rand_prime()
q = rand_prime()

print(" Prime numbers: ", p, "and",q )

# modulus number
n = p * q
print(" modulus number:", n)

# how many numbers are coprime of n
coprime_no = (p - 1) * (q - 1)
print(" How many coprimes: ", coprime_no)

# Get the encryption key
# it be between 1 and coprime_no
# and should be coprime with 'n' and 'coprime_no'

def encrypt_key():
	factors = []
	for i in range(2, coprime_no):
		#if is_prime(i):
		if n % i != 0 and coprime_no % i != 0:
				factors.append(i)
	return factors[-1]

en = encrypt_key()
# the encryption key 
print(" e: ", en," \nEncyption key (public): ", (en, n))


# Decryption key (private key) => 'd'
# 'de' * 'en' mod coprime_no = 1

def decrypt_key(en, coprime_no):
	num = []
	for i in range(1, coprime_no * 2):
		
		if (en * i) % coprime_no == 1:
			num.append (i)
	return num[-1]
	
de = decrypt_key(en,coprime_no)
print(" d:", de, " \ndaecryption key (private): ", (de, n))

# Encrypts a message using RSA
def encrypt(m):
    return str((m**en) % n)

"""Decrypts a message encrypted in RSA"""
def decrypt(c):
    return (c ** de) % n

print("="*53)		
msg = input(" Enter message to encrypt: \n")

encrypted = []
decrypted = []

for c in msg:
    encrypted.append(encrypt(ord(c)))

""" decrypting process"""
for i in encrypted:
    decrypted.append(decrypt(int(i)))
    
deMsg = "".join(list(map(lambda x: chr(x),decrypted)))

""" function that writes the message and the public and private keys into a file"""

def info_to_file():
	
	message = msg
	pub_key = (en, n)
	pri_key = (de, n)
	encrypted_msg = str("".join(encrypted))
	decrypted_msg = deMsg
	
	return {"message": msg, "public key" : pub_key, "private key" : pri_key, "encrypted message" : encrypted_msg, "decrypted message" : decrypted_msg}
	
#file to store the info
try:
	file = open("/sdcard/Python_Codes/Cryptography/file_text.json", "w")
	file.write(" \n")
	
	json.dump(info_to_file(), file, ensure_ascii = False)
except Exception:
	raise
finally:
	file.close()

print("Encrypted Message:")
print("".join(encrypted))


print("\nDecrypted Message:")
print(deMsg)