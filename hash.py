import bcrypt, base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def Hash(password):
    salt = bcrypt.gensalt()
    passwd = bcrypt.hashpw(bytes(password, "utf-8"), salt)
    return passwd.decode("utf-8")

def GenKey(base):
    base = base.encode()
    salt = b"salt_" # change this later
    kdf = PBKDF2HMAC(
        algorithm   = hashes.SHA256(),
        length      = 32,
        salt        = salt,
        iterations  = 100000,
        backend     = default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(base))
    return key