import math
characters = "abcdefghijklmnopqrstuvwxyz"

# #Caeser Cipher

# characters = "abcdefghijklmnopqrstuvwxyz"

# text = input("Enter the text to encrypt:");
# shift = int(input("Enter the shift value:"));



# def encrypt(text, shift):
#     result = ""

#     for i in range(len(text)):
#         char = text[i].lower();
#         char = (characters.index(char) + shift) %26
#         result += characters[char]
#     return result


# def decrypt(text, shift):
#     result = ""

#     for i in range(len(text)):
#         char = text[i].lower();
#         char = (characters.index(char) - shift) %26
#         result += characters[char]
#     return result


# def ceaser_cipher(text, shift):
#     encrypted_text = encrypt(text, shift)
#     decrypted_text = decrypt(encrypted_text, shift)

#     print("Encrypted Text: " + encrypted_text)
#     print("Decrypted Text: " + decrypted_text)


# ceaser_cipher(text, shift)


# #  Vigenere Cipher

# characters = "abcdefghijklmnopqrstuvwxyz"

# text = input("Enter the text to encrypt:").lower();
# key = input("Enter the key:").lower();


# def genrate_key(key):
#     shifts= [];
#     for i in range(len(key)):
#         shifts.append(characters.index(key[i]));
#     return shifts;



# def encrypt_vigenere(text, key):
#     shifts = genrate_key(key)
#     result = ""

#     for i in range (len(text)):
#        shift = shifts[i % len(shifts)];

#        result += characters[(characters.index(text[i]) + shift) % 26];

#     return result;

        

# encrypt_vigenere(text,key)

# def decrypt_vigenere(text, key):
#     shifts = genrate_key(key);
#     result = ""
#     for i in range(len(text)):
#         shift = shifts[i % len(shifts)];

#         result += characters[(characters.index(text[i])-shift) % 26 ]

#     return result;

# def vigenere(text, key):
#     encrypt = encrypt_vigenere(text, key);
#     decrypt = decrypt_vigenere(encrypt,key)

#     print(f'Encrypted text = {encrypt}')
#     print(f'decrypted text = {decrypt}')


# vigenere(text,key)
    
#Affine Cipher


def is_valid(a):
    return math.gcd(a,26) == 1


text = input("enter the text: ").lower().strip();
a = int(input("Enter a:"));
b = int(input("Enter b:"));

def encrypt (text, a, b):
    if is_valid(a): pass
    else: 
        print("value of a is invalid")
        return
    result = ""

    for i in range(len(text)):
      result += characters[((a * characters.index(text[i])) +b) % 26]

    return result


def decrypt (text, a, b):
    result = "" 
    a = pow(a,-1,26)
    for i in range(len(text)):
        result += characters[((a*(characters.index(text[i]) - b)) % 26)]

    return result

def affine(text, a, b):
    encrypt_text = encrypt(text,a,b)
    decrypt_text = decrypt(encrypt_text,a,b)

    print(f"encrypted : {encrypt_text}")
    print(f"decrypted : {decrypt_text}")
        
affine(text,a,b)
