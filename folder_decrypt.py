import os
import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def load_key(key_file):
    """AES anahtarını belirtilen dosyadan yükler."""
    with open(key_file, "rb") as f:
        return f.read()

def decrypt_file(file_path, key):
    """Belirtilen dosyayı AES-256 ile çözer ve şifreli halini siler."""
    with open(file_path, "rb") as f:
        iv = f.read(16)  # İlk 16 byte IV (Initialization Vector)
        ciphertext = f.read()

    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

    original_file_path = file_path.replace(".enc", "")
    with open(original_file_path, "wb") as f:
        f.write(plaintext)

    os.remove(file_path)  # Şifreli dosyayı sil
    print(f"Çözüldü: {original_file_path}")

def decrypt_folder(folder_path, key):
    """Belirtilen klasördeki tüm şifreli dosyaları çözer."""
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".enc"):
                file_path = os.path.join(root, file)
                decrypt_file(file_path, key)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Kullanım: python coz.py aes_key.bin C:\\users\\emre.coskun\\desktop\\deneme")
        sys.exit(1)

    key_file = sys.argv[1]
    folder_to_decrypt = sys.argv[2]

    if not os.path.exists(key_file):
        print("Anahtar dosyası bulunamadı.")
        sys.exit(1)

    if not os.path.exists(folder_to_decrypt):
        print("Çözülecek klasör bulunamadı.")
        sys.exit(1)

    aes_key = load_key(key_file)
    decrypt_folder(folder_to_decrypt, aes_key)

    print("Çözme işlemi tamamlandı.")
