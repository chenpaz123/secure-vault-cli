# Secure Vault CLI 🔐

A robust, command-line password manager built with Python, focusing on security and engineering best practices.
This tool allows users to securely store and retrieve credentials using local AES encryption.

## 🚀 Features

- **AES Encryption:** Uses the `cryptography` library (Fernet) to encrypt passwords before saving to disk.
- **Secure Input:** Utilizes `getpass` to prevent shoulder-surfing during password entry.
- **Data Persistence:** Stores encrypted data in a structured JSON format.
- **Clean Architecture:** Separation of concerns between Logic, Storage, and Presentation layers.
- **Type Safety:** Fully typed code (Type Hints) for reliability.

## 🛠️ Tech Stack

- **Language:** Python 3.12+
- **Dependency Management:** [כתוב כאן את שם הכלי שהשתמשנו בו לניהול חבילות]
- **Security:** `cryptography` (Fernet implementation)

## 📦 Installation

This project uses **Poetry** for dependency management.

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/chenpaz123/secure-vault-cli.git
    cd secure-vault-cli
    ```

2.  **Install dependencies:**
    ```bash
    poetry install
    ```

## 💻 Usage

To run the application, use Poetry to execute the script in the virtual environment:

```bash
poetry run python main.py
```

## Menu Options:

**Add Password:** Encrypts and stores a new credential.

**Get Password:** Decrypts and reveals a stored password.

**Exit:** Closes the secure session.

## ⚠️ Security Note

For security reasons, the secret.key and passwords.json files are NOT included in the repository (via .gitignore).

When you run the app for the first time, a new local encryption key will be generated automatically.

Warning: If you lose your secret.key file, all stored passwords will be unrecoverable!

**👨‍💻 Author**
Chen Paz
