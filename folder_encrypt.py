import os
import sys
import shutil
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def load_key(key_file):
    """AES anahtarını belirtilen dosyadan yükler."""
    with open(key_file, "rb") as f:
        return f.read()

def encrypt_file(file_path, key):
    """Belirtilen dosyayı AES-256 ile şifreler ve orijinalini siler."""
    with open(file_path, "rb") as f:
        plaintext = f.read()
    
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

    enc_file_path = file_path + ".enc"
    with open(enc_file_path, "wb") as f:
        f.write(cipher.iv + ciphertext)

    os.remove(file_path)  # Orijinal dosyayı sil
    print(f"Şifrelendi: {file_path}")

def encrypt_folder(folder_path, key):
    """Belirtilen klasördeki tüm dosyaları şifreler."""
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Kullanım: python sifrele.py aes_key.bin C:\\users\\emre.coskun\\desktop\\deneme")
        sys.exit(1)

    key_file = sys.argv[1]
    folder_to_encrypt = sys.argv[2]

    if not os.path.exists(key_file):
        print("Anahtar dosyası bulunamadı.")
        sys.exit(1)

    if not os.path.exists(folder_to_encrypt):
        print("Şifrelenecek klasör bulunamadı.")
        sys.exit(1)

    aes_key = load_key(key_file)
    encrypt_folder(folder_to_encrypt, aes_key)

    print("Şifreleme tamamlandı.")
