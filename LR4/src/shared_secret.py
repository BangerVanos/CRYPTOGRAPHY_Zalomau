class SharedSecretGenerator:
    PRIMARY_NUMBER = 8699

    @classmethod
    def is_primitive_element(cls, primitive, primary):
        residues = set()
        for i in range(1, primary):
            residue = cls.modulus_pow(primitive, i, primary)
            if residue in residues:
                return False
            residues.add(residue)
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
        alice_mod = cls.modulus_pow(primitive, alice_key, primary)
        bob_mod = cls.modulus_pow(primitive, bob_key, primary)
        if cls.modulus_pow(alice_mod, bob_key, primary) != cls.modulus_pow(bob_mod, alice_key, primary):
            raise ValueError('Shared secrets are not the same!')
        return shared_secret
