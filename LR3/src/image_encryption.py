import PIL.Image
from Crypto.Cipher import AES, DES
from Crypto.Util.Padding import pad


class ImageEncrypter:
    BLOCK_SIZE = 16
    AES_ENCRYPTING_MODES = {'ECB': AES.MODE_ECB,
                            'CBC': AES.MODE_CBC,
                            'CFB': AES.MODE_CFB,
                            'OFB': AES.MODE_OFB,
                            'CTR': AES.MODE_CTR}
    DES_ENCRYPTING_MODES = {'ECB': DES.MODE_ECB,
                            'CBC': DES.MODE_CBC,
                            'CFB': DES.MODE_CFB,
                            'OFB': DES.MODE_OFB,
                            'CTR': DES.MODE_CTR}

    @classmethod
    def encrypt_image(cls, img_path: str, key: str, algorithm: str = 'AES', mode: str = 'ECB'):
        image = PIL.Image.open(img_path)
        ciphertext = ''
        block_size = cls.BLOCK_SIZE if mode != 'CTR' else cls.BLOCK_SIZE * 4
        if algorithm == 'AES':
            cipher = AES.new(key.encode('utf-8'), cls.AES_ENCRYPTING_MODES[mode])
            ciphertext = cipher.encrypt(pad(image.tobytes(), block_size))
        elif algorithm == 'DES':
            cipher = DES.new(key.encode('utf-8'), cls.DES_ENCRYPTING_MODES[mode])
            ciphertext = cipher.encrypt(pad(image.tobytes(), block_size))
        image = PIL.Image.frombytes(mode='RGB', size=image.size, data=ciphertext)
        image.save('images/encrypted.jpg')
