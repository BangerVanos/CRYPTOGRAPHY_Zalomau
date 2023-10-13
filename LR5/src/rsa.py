from Crypto.Util.number import getStrongPrime


class RSA:
    PRIME_BITS_AMOUNT = 1024
    OPEN_EXPONENT = 65537

    @classmethod
    def egcd(cls, num_1, num_2):
        s = 0
        old_s = 1
        t = 1
        old_t = 0
        r = num_2
        old_r = num_1
        while r != 0:
            quotient = old_r // r
            old_r, r = r, old_r - quotient * r
            old_s, s = s, old_s - quotient * s
            old_t, t = t, old_t - quotient * t
        return old_r, old_s, old_t

    @classmethod
    def modular_inv(cls, num_1, num_2):
        gcd, x, y = cls.egcd(num_1, num_2)
        if x <= 0:
            x += num_2
        return x

    @classmethod
    def generate_key(cls):
        p = getStrongPrime(1024)
        q = getStrongPrime(1024)
        n = p * q
        phi = (p - 1) * (q - 1)
        d = cls.modular_inv(cls.OPEN_EXPONENT, phi)
        return {'open_key': {'e': cls.OPEN_EXPONENT, 'n': n},
                'close_key': {'d': d, 'n': n}}

    @classmethod
    def encrypt_message(cls, message: str, key: dict) -> list[int]:
        symbol_list = list(message)
        return list(map(lambda x: pow(ord(x), key['e'], key['n']), symbol_list))

    @classmethod
    def decrypt_message(cls, message: list[int], key: dict):
        return ''.join(list(map(lambda x: chr(pow(x, key['d'], key['n'])), message)))
