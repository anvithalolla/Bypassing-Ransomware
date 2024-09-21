from zipfile import ZipFile
import sys

def attempt_extract(zf_handle, password):
    try:
        # Attempt to extract the zip file using the given password
        zf_handle.extractall(pwd=password.strip())
        print(f"[+] Password found: {password.decode().strip()}")
        return True
    except RuntimeError as e:
        # Handle incorrect password attempts
        if 'Bad password' in str(e):
            return False
        else:
            print(f"[-] An error occurred: {e}")
            sys.exit(1)
    except Exception as e:
        print(f"[-] An unexpected error occurred: {e}")
        sys.exit(1)

def main():
    print("[+] Beginning bruteforce")

    with ZipFile('enc.zip') as zf:
        with open('rockyou.txt', 'rb') as f:
            for line in f:
                password = line.strip()
                if attempt_extract(zf, password):
                    break
            else:
                print("[+] Password not found in list")

if __name__ == "__main__":
    main()
