from cipher import EncryptionManager
from storage import StorageManager
import getpass
import os

SECRET_KEY_FILE = "secret.key"
PASSWORD_DB = "passwords.json"


def get_or_create_key() -> bytes:
    """Loads the key from file or generates a new one if missing."""
    if os.path.exists(SECRET_KEY_FILE):
        with open(SECRET_KEY_FILE, "rb") as key_file:
            return key_file.read()
    else:
        new_key = EncryptionManager.generate_key()
        with open(SECRET_KEY_FILE, "wb") as key_file:
            key_file.write(new_key)
        return new_key


def main():
    # 1. Setup Infrastructure
    storage = StorageManager(PASSWORD_DB)

    key = get_or_create_key()
    crypto_manager = EncryptionManager(key)

    # 3. Main Loop
    while True:
        print("\n=== Secure Password Vault ===")
        print("1. Add Password")
        print("2. Get Password")
        print("3. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            service = input("Enter service name: ")
            username = input("Enter username: ")
            # getpass ensures the password isn't visible on screen
            password = getpass.getpass("Enter password: ")

            # Encrypt and Decode to String for JSON
            encrypted_token = crypto_manager.encrypt(password)
            encrypted_str = encrypted_token.decode("utf-8")

            # Load, Update, Save
            data = storage.load_data()
            data[service] = {"username": username, "password": encrypted_str}
            storage.save_data(data)
            print(f"✅ Password for {service} saved successfully!")

        elif choice == "2":
            service = input("Enter service name: ")
            data = storage.load_data()

            if service in data:
                record = data[service]
                encrypted_str = record["password"]

                # Encode back to Bytes for Decryption
                try:
                    decrypted_pass = crypto_manager.decrypt(
                        encrypted_str.encode("utf-8")
                    )
                    print(f"\n🔑 Service: {service}")
                    print(f"👤 Username: {record['username']}")
                    print(f"🔓 Password: {decrypted_pass}")
                except Exception:
                    print(
                        "❌ Error: Failed to decrypt password (Integrity check failed)."
                    )
            else:
                print("❌ Service not found.")

        elif choice == "3":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()
