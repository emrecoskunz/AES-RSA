from Crypto.PublicKey import RSA

def generate_rsa_keys():
    """RSA 4096-bit özel ve açık anahtar üret ve dosyalara kaydet."""
    key = RSA.generate(4096)

    # Özel anahtarı kaydet
    with open("private_key.pem", "wb") as priv_file:
        priv_file.write(key.export_key())

    # Açık anahtarı kaydet
    with open("public_key.pem", "wb") as pub_file:
        pub_file.write(key.publickey().export_key())

    print("RSA 4096-bit anahtar çifti oluşturuldu ve kaydedildi.")

if __name__ == "__main__":
    generate_rsa_keys()
