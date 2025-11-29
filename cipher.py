from cryptography.fernet import Fernet


class EncryptionManager:

    def __init__(self, key: bytes):
        """constructor method
        args:
            key (bytes): The encryption key in bytes.
        """

        self.fernet = Fernet(key)

    def encrypt(self, data: str) -> bytes:
        """
        encrypt method:
        Encrypts the given data string and returns the encrypted bytes.
        args:
            data (str): The string data to be encrypted.
        returns:
            bytes: The encrypted data in bytes.
        """
        return self.fernet.encrypt(data.encode())

    def decrypt(self, token: bytes) -> str:
        """
        decrypt method:
        Decrypts the given encrypted bytes and returns the original string.
        args:
            token (bytes): The encrypted data in bytes.
        returns:
            str: The decrypted original string.
        """
        return self.fernet.decrypt(token).decode()

    @staticmethod
    def generate_key() -> bytes:
        """static method to generate a new key
        returns:
            bytes: The generated key in bytes.
        """
        return Fernet.generate_key()
