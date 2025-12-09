# Python File Encryption & Decryption Tool

A secure, command-line based file encryption tool built in Python, using the library `cryptography`. This project implements **Symmetric Encryption** through the module Fernet to warrant data confidentiality and integrity.

Theoretical Concepts

This project demonstrates several cybersecurity key concepts:

1. Symmetric Encryption
This tool uses **Symmetric-key algorithms**, meaning the *same key* is used for both encrypting (locking) and decrypting (unlocking) the data.
* Fast and efficient in handling a large amount of data.

* **Cons:** Key distribution is critical - if you share the encrypted file, you need to securely share the key as well.
2. Fernet (The Implementation)
I used **Fernet**, a system given by the library `cryptography`. Fernet makes sure that any message encrypted with it can neither be manipulated nor read without the key.

* **Under the hood:** Fernet uses **AES (Advanced Encryption Standard)** in CBC mode with a 128-bit key for encryption and **HMAC** using SHA256 for authentication.
* **Base64 Encoding:** The keys and tokens are URL-safe base64-encoded bytes, making them safe to send via email or store in databases.

3. CIA Triad (Confidentiality & Integrity)

Confidentiality: The file content is unreadable for anyone without the key.
* **Integrity:** Fernet includes a signing token. This means that, in case a hacker tries to alter the encrypted file-for example, by flipping bits-the decryption will fail since the signature won't match.
---
## Features

* **Key Generation:** Creates by default a secure, random 256-bit key (`secret.key`).
* **Encrypt Data:** Transforms plain text files into unreadable ciphertext.

* **Decrypt Data:** Restores original files using the matching key.
* * **Error Handling**: It finds the missing keys or files and avoids crashes.
---
### Technologies Used 

* **Language:** Python 3.11.3
* * **Library:** `cryptography` ---
