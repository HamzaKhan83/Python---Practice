import hmac
import hashlib
from hashlib import sha256
from inspect import signature

print(hashlib.sha256(b"hello").hexdigest())

print(hashlib.sha256(b"hello").hexdigest())


def hash_text(text):

    # MD5
    md5_hash = hashlib.md5(text.encode()).hexdigest()
    print(f"MD5 (128 bit): {md5_hash}")

    # SHA-1
    sha1_hash = hashlib.sha1(text.encode()).hexdigest()
    print(f"SHA-1 (160 bit): {sha1_hash}")

    # SHA-256
    sha256_hash = hashlib.sha256(text.encode()).hexdigest()
    print(f"SHA-256 (256 bit): {sha256_hash}")

    # SHA-512
    sha512_hash = hashlib.sha512(text.encode()).hexdigest()
    print(f"SHA-512 (512 bit): {sha512_hash}")

    print("" * 60)


hash_text("hello world")

hash_text("hello world hamza")

key = b"SecretApiKey"
message = b"Transfer $100 to Bob"
signature = hmac.new(key, message, hashlib.sha256).hexdigest()


def generate_hmac(key, message):
    """Genreate HMAC signature."""
    return hmac.new(key, message.encode(), sha256).hexdigest()


def verify_hmac(key, message, received_signature):
    """Verify HMAC signature."""
    expected_signature = generate_hmac(key, message)
    return hmac.compare_digest(expected_signature, received_signature)


secret_key = b"SuperSecretApiKey123"
message = "Transfer $100 to Alice"


signature = generate_hmac(secret_key, message)
print("Message = ", message)
print("Signature = ", signature)

print("/n ---- Verification ----")
print("Valid Message? ", verify_hmac(secret_key, message, signature))

tampered = "Transfer $1000000 to Alice"
print("Tampered ", tampered)
print("Valid Message? ", verify_hmac(secret_key, tampered, signature))

generate_hmac(secret_key, message)
verify_hmac(secret_key, tampered, signature)


def get_file_hash(file_path, algorithm="sha256"):
    hasher = getattr(hashlib, algorithm)()
    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            hasher.update(chunk)
    return hasher.hexdigest()


print(get_file_hash("data"))
