from Crypto.Cipher import DES, AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

key = get_random_bytes(32)
iv = get_random_bytes(16)



with open("original.txt", "rb") as file:
    data = file.read()

cipher = AES.new(key, AES.MODE_CBC, iv)
ct = cipher.encrypt(pad(data, AES.block_size))

with open("key.bin", "wb") as key_file:
    key_file.write(key+iv)


with open("encrypted.bin", "wb") as file:
    file.write(ct)

print("File encrypted successfully.")

with open("key.bin", "rb") as file: 
    data2 = file.read()

key = data2[:32]
iv = data2[32:48]

with open("encrypted.bin","rb") as file: 
    ct = file.read()

cipher2 = AES.new(key, AES.MODE_CBC, iv)

dt = unpad(cipher2.decrypt(ct), AES.block_size)

with open("decrypted.txt", "wb") as file:
    file.write(dt)

print("File decrypted successfully.")


with open("original.txt", "rb") as file:
    original = file.read()

with open("decrypted.txt", "rb") as file:
    decrypted = file.read()

if original == decrypted:
    print("Files match!")
else:
    print("Files do not match!")