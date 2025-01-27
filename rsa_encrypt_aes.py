import sys
import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def encrypt_aes_key(aes_key_file, public_key_file):
    """AES anahtarını RSA açık anahtarı ile şifreler ve ardından AES anahtar dosyasını siler."""
    with open(aes_key_file, "rb") as f:
        aes_key = f.read()

    with open(public_key_file, "rb") as f:
        public_key = RSA.import_key(f.read())

    cipher_rsa = PKCS1_OAEP.new(public_key)
    encrypted_key = cipher_rsa.encrypt(aes_key)

    with open("aes_key_encrypted.bin", "wb") as f:
        f.write(encrypted_key)

    os.remove(aes_key_file)  # AES anahtar dosyasını sil
    print(f"AES anahtarı başarıyla RSA ile şifrelendi ve '{aes_key_file}' silindi.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Kullanım: python rsa_encrypt_aes.py aes_key.bin public_key.pem")
        sys.exit(1)

    encrypt_aes_key(sys.argv[1], sys.argv[2])
