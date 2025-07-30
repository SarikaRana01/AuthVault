from cryptography.fernet import Fernet,InvalidToken
from django.conf import settings

fernet = Fernet(settings.ENCRYPTION_KEY.encode())

def encrypt_password(password):
    return fernet.encrypt(password.encode()).decode()



def decrypt_password(encrypted_password):
    try:
        return fernet.decrypt(encrypted_password.encode()).decode()
    except (InvalidToken, AttributeError) as e:
        print(f"[Decryption Error] Problem with: {encrypted_password}")
        return "[Decryption Failed]"