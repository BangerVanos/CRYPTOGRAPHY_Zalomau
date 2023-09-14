class ScytaleCipher:
    @staticmethod
    def encode_message(message: str, key: int, ignore_spaces: bool = False, debug: bool = False) -> str:
        """Method for encoding your message. All spaces (if not ignored, check 'ignore_spaces' flag)
        will be replaced with '_' symbol. If there is too much space in the table '_' also will be used.
        If you want to see scytale table, use True with 'debug' flag"""
        message = message.replace(' ', '' if ignore_spaces else '_')
        cols_amount = int((len(message) - 1)/key) + 1
        scytale_table = [[message[i + j * cols_amount] if (i + j * cols_amount) < len(message) else '_'
                          for i in range(cols_amount)] for j in range(key)]
        if debug:
            print('-'*10)
            print('Scytale cipher table:')
            print('\n'.join(['|'.join(row) for row in scytale_table]))
            print('-' * 10)
        scytale_table = list(zip(*scytale_table))
        return ''.join([''.join(row) for row in scytale_table])

    @staticmethod
    def decode_message(message: str, key: int) -> str:
        """Method for decoding encoded message. All you need is decoded message
        and key, which is scytale cylinder diameter"""
        cols_amount = int((len(message) - 1) / key) + 1
        scytale_table = [[message[i + j * key] for i in range(key)] for j in range(cols_amount)]
        scytale_table = list(zip(*scytale_table))
        return ''.join([''.join(row) for row in scytale_table])

    @classmethod
    def bruteforce_attack(cls, message: str, encoded_message: str) -> int:
        """Method for checking fastness of brute force for this cipher (spoiler, it will be very fast).
        Just put here encoded and original messages. As main task of cryptoanalysis for Scytale cipher
        is only to get sense os message all of '_' and space symbols in original
        and 'decoded' messages are removed for proper check. Method will return the key (scytale cylinder diameter)"""
        key = 1
        message = message.replace('_', '').replace(' ', '')
        while message != cls.decode_message(encoded_message, key).replace('_', ''):
            key += 1
        return key


class ScytaleCipherImproved(ScytaleCipher):
    """Small upgrade for Scytale cipher. Firstly, message will be encoded with Caesar's cipher.
    Then Scytale cipher will be used. So now you'll need two keys for encoding.
    For proper work spaces will not be ignored in any case."""
    UNICODE_MAX_VALUE = 1114111

    @classmethod
    def improved_encode_message(cls, message: str, keys: tuple[int, int]) -> str:
        message = ''.join([chr(ord(sym) + keys[0] % cls.UNICODE_MAX_VALUE) for sym in message])
        return cls.encode_message(message, keys[1], False, False)

    @classmethod
    def improved_decode_message(cls, message: str, keys: tuple[int, int]) -> str:
        message = cls.decode_message(message, keys[1])
        return ''.join([chr(ord(sym) - keys[0] % cls.UNICODE_MAX_VALUE) for sym in message])
