from Crypto.Cipher import DES, AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


# key = get_random_bytes(8)

# cipher = DES.new(key, DES.MODE_ECB)

# ciphered_text = cipher.encrypt(pad(b"Hamza",8))

# cipher2 = DES.new(key, DES.MODE_ECB)
# decyphered_text = unpad(cipher2.decrypt(ciphered_text),8)

# print(ciphered_text.hex())

# print(decyphered_text.decode())


# DES VS AES

# des_key = get_random_bytes(8)
# aes_key = get_random_bytes(16)

# des_cipher = DES.new(des_key, DES.MODE_ECB)
# aes_cipher = AES.new(aes_key, AES.MODE_ECB)

# des_ct = des_cipher.encrypt(pad(b"Hamza", 8))
# aes_ct = aes_cipher.encrypt(pad(b"Hamza", 16))

# des_cipher2 = DES.new(des_key, DES.MODE_ECB)
# aes_cipher2 = AES.new(aes_key, AES.MODE_ECB)

# des_dt = unpad(des_cipher2.decrypt(des_ct),8)
# aes_dt = unpad(aes_cipher2.decrypt(aes_ct),16)


# print("DES:", des_ct.hex())
# print(des_dt.decode())
# print("AES:", aes_ct.hex())
# print(aes_dt.decode())

# ECB VS CBC


key = get_random_bytes(16)
iv = get_random_bytes(16)

message = b"Hamza"

ecb_cipher = AES.new(key, AES.MODE_ECB)
cbc_cipher = AES.new(key, AES.MODE_CBC, iv)

ecb_ct = ecb_cipher.encrypt(pad(message, 16))
cbc_ct = cbc_cipher.encrypt(pad(message, 16))

print("ECB Ciphertext:", ecb_ct.hex())
print("CBC Ciphertext:", cbc_ct.hex())

ecb_cipher2 = AES.new(key, AES.MODE_ECB)
cbc_cipher2 = AES.new(key, AES.MODE_CBC, iv)

ecb_dt = unpad(ecb_cipher2.decrypt(ecb_ct), 16)
cbc_dt = unpad(cbc_cipher2.decrypt(cbc_ct), 16)

print("ECB Decrypted:", ecb_dt.decode())
print("CBC Decrypted:", cbc_dt.decode())



