import sys
import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def decrypt_aes_key(encrypted_key_file, private_key_file):
    """RSA özel anahtarı ile AES anahtarını çözer ve ardından şifreli dosyayı siler."""
    with open(encrypted_key_file, "rb") as f:
        encrypted_key = f.read()

    with open(private_key_file, "rb") as f:
        private_key = RSA.import_key(f.read())

    cipher_rsa = PKCS1_OAEP.new(private_key)
    aes_key = cipher_rsa.decrypt(encrypted_key)

    with open("aes_key_decrypted.bin", "wb") as f:
        f.write(aes_key)

    os.remove(encrypted_key_file)  # Şifreli AES anahtar dosyasını sil
    print(f"AES anahtarı başarıyla çözüldü ve '{encrypted_key_file}' silindi.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Kullanım: python rsa_decrypt_aes.py aes_key_encrypted.bin private_key.pem")
        sys.exit(1)

    decrypt_aes_key(sys.argv[1], sys.argv[2])
