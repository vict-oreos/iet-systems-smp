import hashlib
import secrets
PASSWORD="IETNITK"
def hash_sha(password:str)->str:
    return hashlib.sha256(password.encode()).hexdigest()
def hash_salt(password:str)->str:
    salt=secrets.token_bytes(16) 
    combined=salt+password.encode()
    digest=hashlib.sha256(combined).hexdigest()
    return digest
def main():
    print(f"Hash with SHA-256 {hash_sha(PASSWORD)}\n")
    print(f"Hash in first run (salted): {hash_salt(PASSWORD)}\n")
    print(f"Hash in second run (salted): {hash_salt(PASSWORD)}\n")
main()
