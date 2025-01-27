import os

def generate_aes_key():
    """256 bit (32 byte) AES anahtarı üretir ve dosyaya kaydeder."""
    key = os.urandom(32)  # 256-bit AES anahtarı (32 byte)
    with open("aes_key.bin", "wb") as key_file:
        key_file.write(key)

if __name__ == "__main__":
    generate_aes_key()
