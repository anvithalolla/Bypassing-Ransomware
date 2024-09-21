# Ransomware Decryption Key Brute-Forcing

## Task Description

This project involves creating a Python script to brute-force the decryption key of an encrypted zip file. The aim is to recover access to the file without paying a ransom, as there is no guarantee that attackers will provide the decryption key or refrain from future attacks. The task focuses on using a wordlist to attempt various passwords until the correct one is found.

## Task Overview

The project demonstrates how to:
- Understand what 'bruteforcing' involves.
- Use Python to respond to a ransomware attack by attempting to decrypt an encrypted file.
- Write a Python script that iterates through potential passwords to find the correct decryption key.

## Files and Necessary Prerequisites

### Files
- `bruteforce_decrypt.py`: The main Python script for brute-forcing the decryption key.
- `enc.zip`: The encrypted zip file that needs decryption.
- `rockyou.txt`: A wordlist file containing potential passwords.

### Prerequisites
- Python 3.x installed on your system.
- `zipfile` module (part of Python's standard library).
- A wordlist file (`rockyou.txt`) which can be downloaded from various online sources if not already available.

## Description of `bruteforce_decrypt.py`

The `bruteforce_decrypt.py` script is designed to attempt password extraction on an encrypted zip file using a provided wordlist. It reads each password from the wordlist, tries it on the zip file, and prints out the correct password once found. The script handles errors gracefully, exiting if unexpected issues occur.

### Key Functions
- **`attempt_extract(zf_handle, password)`**: Tries to extract the zip file using a given password. If successful, it prints the password and returns `True`. If not, it continues with the next password.
- **`main()`**: Orchestrates the brute-force process by opening the zip file and reading through the wordlist. It calls `attempt_extract` for each password until it finds the correct one or exhausts all options.

## Conclusion

This project provides a practical approach to handling ransomware situations where only one file is affected. By using a brute-force method with a common wordlist, we can potentially recover access without succumbing to ransom demands. This method relies on the assumption that attackers may use weak or common passwords due to carelessness.

