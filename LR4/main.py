from src.shared_secret import SharedSecretGenerator


if __name__ == '__main__':
    primitive_element = SharedSecretGenerator.find_primitive(SharedSecretGenerator.PRIMARY_NUMBER)
    print(f'Primitive element for {SharedSecretGenerator.PRIMARY_NUMBER} is {primitive_element}')
    alice_key, bob_key = 25, 15
    shared_secret = SharedSecretGenerator.generate_shared_secret(SharedSecretGenerator.PRIMARY_NUMBER,
                                                                 primitive_element, alice_key, bob_key)
    print(f'Shared secret for Alice\'s key being {alice_key} and Bob\'s key being {bob_key} is '
          f'{shared_secret}')
