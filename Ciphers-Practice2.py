import secrets


from Crypto.Cipher import Salsa20
from Crypto.Random import get_random_bytes

plaintext = input("Enter the message: ").encode()
key = get_random_bytes(32)

cipher = Salsa20.new(key=key)

nonce = cipher.nonce

ciphertext = cipher.encrypt(plaintext)

cipher2 = Salsa20.new(key=key, nonce=nonce)
decrypted = cipher2.decrypt(ciphertext)

print("Key (hex):       ", key.hex())
print("Nonce (hex):     ", nonce.hex())
print("Ciphertext (hex):", ciphertext.hex())
print("Decrypted:       ", decrypted.decode())

if decrypted == plaintext:
    print("Verification: decryption matches the original")
else:
    print("Verification FAILED")

#Vernam Cipher Practice 

# text = input("Enter the text: ")
# key = input("Enter the key:")

# def vernam_encrypt (text, key):
#     result = ""


#     for i in range (len(text)):
#         result += chr(ord(text[i]) ^ ord(key[i % len(key)]))

#     return result;


# def vernam_decrypt (text, key):

#     result = ""

#     for i in range(len(text)):
#         result += chr(ord(text[i]) ^ ord(key[i % len(key)]))
#     return result

# def vernam(text, key):
#     encrypted = vernam_encrypt(text, key)
#     decrypted = vernam_decrypt(encrypted, key)

#     print(f"Your encrypted text is {encrypted}")
#     print(f"Your decrypted text is {decrypted}")

# vernam(text, key)


# PRG ANALYSIS RANDOM NUMBER GENERATION

# bits = int(input("Enter the number of bits: "))


# key = []
# message = []

# for i in range(bits):
#     key.append(secrets.randbits(1))

# for i in range(bits):
#     message.append(secrets.randbits(1))

# cipher = []

# for i in range (bits):
#     cipher.append(message[i] ^ key[i])

# decrypt = []

# for i in range (bits):
#     decrypt.append(cipher[i] ^ key[i])


# print(f"The key is {key}")
# print(f"The message is {message}")
# print(f"The cipher is {cipher}")
# print(f"The decrypt is {decrypt}")

# if message == decrypt:
#     print("Validation is true. ")
# else: 
#     print("The validation is incorrect")


