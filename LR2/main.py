from src.scytale_cipher import ScytaleCipher, ScytaleCipherImproved


if __name__ == '__main__':
    message = 'Hello world from space'
    key = 2
    encoded_message = ScytaleCipher.encode_message(message, key, False, True)
    print(f'Original message: {message}\nEncoded message: {encoded_message}\n'
          f'Decoded message: {ScytaleCipher.decode_message(encoded_message, key)}')
    print(f'Key you use for your message is: {ScytaleCipher.bruteforce_attack(message, encoded_message)}')
    improved_cipher_keys = (10, 2)
    encoded_message = ScytaleCipherImproved.improved_encode_message(message, improved_cipher_keys)
    print(f'Encoded message (improved cipher): {encoded_message}\n'
          f'Decoded message (improved cipher): '
          f'{ScytaleCipherImproved.improved_decode_message(encoded_message, improved_cipher_keys)}')
