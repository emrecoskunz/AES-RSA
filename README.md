# AES-RSA

AES ve RSA ile Güvenli Şifreleme ve Çözme Klavuzu
Günümüzde, veri güvenliği her zamankinden daha önemli. Bu klavuz, AES ve RSA algoritmalarını bir arada kullanarak dosyalarınızı şifrelemenizi ve güvenle saklamanızı sağlar. AES, güçlü bir simetrik şifreleme algoritmasıdır, ancak tek başına kullanıldığında anahtarın güvenliği büyük önem taşır. Bu nedenle, AES anahtarınızı RSA ile şifreleyerek, anahtarınızı da koruma altına alacağız. Bu kombinasyon, güvenliği maksimuma çıkaran bir çözüm sunar.

AES anahtarı simetrik şifreleme için kullanılırken, RSA ise asimetrik şifreleme sağlayarak anahtar güvenliğinizi artırır. Bu sayede, AES anahtarınızın güvenliği, RSA'nın güçlü şifreleme özellikleriyle sağlanır. Hadi adım adım nasıl çalıştığını görelim.

1. AES Anahtarı Oluşturma
İlk olarak, AES algoritmasıyla bir anahtar oluşturuyoruz. AES anahtarı, şifreleme işleminin temel taşıdır. Şifreleyeceğimiz verilerin güvenliğini sağlayacak olan bu anahtarı, güçlü ve rastgele bir şekilde oluşturuyoruz. Bu anahtarın kırılması imkansız olmasa da, modern bilgisayarlarla bile neredeyse imkansızdır. AES-256, şifreleme dünyasında en güçlü algoritmalardan biri olarak kabul edilir.

Kullanım:
```python
python aes_keygen.py
```

Bu komut çalıştırıldığında, aes_key.bin adlı bir dosya oluşturulacak. Bu dosya, AES algoritması ile şifreleme işlemlerinde kullanılacak güçlü anahtarınızı barındıracak.

2. Folderi AES Anahtarı ile Şifreleme
AES anahtarımızı oluşturduktan sonra, artık klasörlerimizi şifrelemeye geçebiliriz. Bu işlem, klasördeki tüm dosyaları AES anahtarı ile şifreleyecek ve dosyalar kırılması son derece zor bir biçimde korunacak. Şifrelenmiş dosyalar, orijinal halleriyle erişilemez hâle gelir. Bu sayede, dosyalarınız çok güçlü bir güvenlik korumasına sahip olacak.

Kullanım:
```python
python folder_encrypt.py aes_key.bin "C:\\path\\to\\your\\folder"
```

Bu komut, belirtilen klasörü ve içindeki tüm dosyaları AES anahtarınızla şifreleyecek. Şifrelenmiş dosyalar aynı klasörde kaydedilecektir.

3. RSA Anahtarı Oluşturma
AES anahtarınızı daha güvenli bir şekilde saklamak için RSA algoritmasını kullanacağız. RSA, asimetrik şifrelemenin lider algoritmalarından biridir ve uzun anahtarlar ile yüksek güvenlik sağlar. RSA ile, AES anahtarınızı şifreleyerek onu güvenli bir şekilde koruyacağız. RSA anahtarı ile şifrelenen AES anahtarı, yalnızca özel RSA anahtarınızla çözülebilir, böylece üçüncü şahıslar tarafından erişilmesi imkansız hale gelir.

RSA anahtar çiftini oluşturduğumuzda, bir açık anahtar (public_key.pem) ve bir özel anahtar (private_key.pem) oluşturulacaktır. Özel anahtarınız, yalnızca sizin erişebileceğiniz şekilde saklanmalıdır.

Kullanım:
```python
python rsa_keygen.py
```

Bu komut, iki dosya oluşturacak:

private_key.pem → RSA özel anahtarı.
public_key.pem → RSA açık anahtarı.

4. RSA Anahtarı ile AES Anahtarını Şifreleme
Şimdi, oluşturduğumuz RSA açık anahtarını kullanarak AES anahtarını şifreleyeceğiz. Bu işlemle birlikte, AES anahtarının güvenliği büyük ölçüde artacak. Çünkü şifrelenen AES anahtarı yalnızca RSA özel anahtarınızla çözülebilir.

Kullanım:
```python
python rsa_encrypt_aes.py aes_key.bin public_key.pem
```

Bu komut şu işlemi yapacak:

aes_key.bin dosyasındaki AES anahtarını RSA açık anahtarı ile şifreleyecek.
Şifrelenmiş AES anahtarı aes_key_encrypted.bin olarak kaydedilecek.
AES anahtar dosyasının orijinali silinecek, böylece yalnızca şifrelenmiş AES anahtarı kalacak.
5. RSA Anahtarı ile Şifrelenen AES Anahtarını Çözme
RSA özel anahtarınızı kullanarak, şifrelenmiş AES anahtarını çözebilirsiniz. Bu adımda, şifrelenmiş AES anahtarını çözerek tekrar kullanabiliriz. Bu işlemi gerçekleştirmek, veri güvenliğinizin bozulmadan dosyalarınıza erişim sağlamanızı sağlar.

Kullanım:
```python
python rsa_decrypt_aes.py aes_key_encrypted.bin private_key.pem
```

Bu komut şunları yapacak:

aes_key_encrypted.bin dosyasındaki AES anahtarını RSA özel anahtarı ile çözecek.
Çözülen AES anahtarı aes_key_decrypted.bin olarak kaydedilecek.
Şifreli AES anahtar dosyası silinecek, böylece güvenlik sağlanmış olacak.
6. Çözülen AES Anahtarı ile Şifrelenen Folderi Çözme
Şimdi, çözülen AES anahtarını kullanarak şifrelenmiş klasörü çözebiliriz. Bu işlem, şifrelenmiş dosyaların orijinal haline geri dönmesini sağlayacak. Dosyalar, güvenli bir şekilde korunmuş olsalar da, doğru AES anahtarına sahip olduğunuzda tekrar erişilebilir olacak.

Kullanım:
```python
python folder_decrypt.py aes_key_decrypted.bin "C:\\path\\to\\your\\encrypted_folder"
```

Bu komut, şifreli klasördeki tüm dosyaları çözecek ve orijinal hâllerine geri getirecektir.

Güvenlik Notları
RSA özel anahtarınız kesinlikle güvenli bir yerde saklanmalıdır. Eğer özel anahtar kaybolursa, şifrelenmiş AES anahtarını ve dolayısıyla şifrelenmiş dosyalarınızı geri almanız mümkün olmaz.
Her işlem sonrasında, şifrelenmiş ve çözülen anahtar dosyaları otomatik olarak silinir. Bu, ekstra güvenlik katmanı sağlar ve iz bırakmadan şifreleme işlemleri yapılmasını mümkün kılar.
AES ve RSA şifreleme yöntemleri güçlü ve kırılması çok zor sistemlerdir. AES-256, günümüz bilgisayarları ile çözülmesi neredeyse imkansız olan bir algoritmadır. RSA ise asimetrik şifrelemede en güvenli seçeneklerden biridir.

Özet

AES Anahtarı Oluşturma: ```python python aes_keygen.py ```

Folderi AES ile Şifreleme: ```python python folder_encrypt.py aes_key.bin "C:\\path\\to\\your\\folder" ```

RSA Anahtarı Oluşturma: ```python python rsa_keygen.py ```

RSA Anahtarı ile AES Anahtarını Şifreleme: ```python python rsa_encrypt_aes.py aes_key.bin public_key.pem ```

RSA Anahtarı ile Şifrelenmiş AES Anahtarını Çözme: ```python python rsa_decrypt_aes.py aes_key_encrypted.bin private_key.pem ```

AES Anahtarı ile Şifrelenmiş Folderi Çözme: ```python python folder_decrypt.py aes_key_decrypted.bin "C:\\path\\to\\your\\encrypted_folder" ```
