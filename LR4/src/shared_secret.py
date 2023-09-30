class SharedSecretGenerator:
    PRIMARY_NUMBER = 8699

    @classmethod
    def is_primitive_element(cls, primitive, primary):
        pow_mod_remainders = set()
        for i in range(1, primary):
            remainder = cls.modulus_pow(primitive, i, primary)
            if remainder in pow_mod_remainders:
                return False
            pow_mod_remainders.add(remainder)
        return True

    @classmethod
    def modulus_pow(cls, base, exponent, mod=1):
        if exponent == 0:
            return 1
        result = 1
        while exponent != 0:
            if exponent % 2 != 0:
                result *= base
                result %= mod
                exponent -= 1
            else:
                base *= base
                base %= mod
                exponent /= 2
        return result

    @classmethod
    def find_primitive(cls, primary: int):
        for primitive in range(2, primary):
            if cls.is_primitive_element(primitive, primary):
                return primitive
        return None

    @classmethod
    def generate_shared_secret(cls, primary, primitive, alice_key, bob_key):
        shared_secret = cls.modulus_pow(primitive, alice_key * bob_key, primary)
        alice_open = cls.modulus_pow(primitive, alice_key, primary)
        bob_open = cls.modulus_pow(primitive, bob_key, primary)
        if cls.modulus_pow(alice_open, bob_key, primary) != cls.modulus_pow(bob_open, alice_key, primary):
            raise ValueError('Shared secrets are not the same!')
        return shared_secret
