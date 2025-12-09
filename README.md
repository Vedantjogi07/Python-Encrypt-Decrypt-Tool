# 🔐 Python File Encryption & Decryption Tool

A secure, command-line based file encryption tool built using Python and the `cryptography` library. This project implements **Symmetric Encryption** using the Fernet module to ensure data confidentiality and integrity.

## 📖 Theoretical Concepts

This project demonstrates several core cybersecurity concepts:

### 1. Symmetric Encryption
This tool uses **Symmetric-key algorithms**, meaning the *same key* is used for both encrypting (locking) and decrypting (unlocking) the data.
* **Pros:** Fast and efficient for large amounts of data.
* **Cons:** Key distribution is critical—if you share the encrypted file, you must securely share the key as well.

### 2. Fernet (The Implementation)
I utilized **Fernet**, a system provided by the `cryptography` library. Fernet guarantees that a message encrypted using it cannot be manipulated or read without the key.
* **Under the hood:** Fernet uses **AES (Advanced Encryption Standard)** in CBC mode with a 128-bit key for encryption and **HMAC** using SHA256 for authentication.
* **Base64 Encoding:** The keys and tokens are URL-safe base64-encoded bytes, making them safe to send via email or store in databases.

### 3. CIA Triad (Confidentiality & Integrity)
* **Confidentiality:** The file content is unreadable to anyone without the key.
* **Integrity:** Fernet includes a signing token. If a hacker tries to modify the encrypted file (e.g., flipping bits), the decryption will fail because the signature won't match.

---

## 🚀 Features
* **Key Generation:** Automatically generates a secure, random 256-bit key (`secret.key`).
* **Encrypt Data:** Converts plain text files into unreadable ciphertext.
* **Decrypt Data:** Restores original files using the matching key.
* **Error Handling:** Detects missing keys or files to prevent crashes.

## 🛠️ Technologies Used
* **Language:** Python 3.x
* **Library:** `cryptography`

---
