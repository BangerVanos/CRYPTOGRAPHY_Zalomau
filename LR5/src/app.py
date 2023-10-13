import flet as ft
import json
from .rsa import RSA


def rsa_app_page(page: ft.Page):

    def generate_keys(e):
        keys = RSA.generate_key()
        with open('close_key.txt', 'w') as file:
            json.dump(keys['close_key'], file)
        with open('open_key.txt', 'w') as file:
            json.dump(keys['open_key'], file)
        open_key_field.value = f'Open key: {keys["open_key"]}'
        close_key_filed.value = f'Close key: {keys["close_key"]}'
        page.update()

    def encrypt_message(e):
        with open('open_key.txt', 'r') as file:
            open_key = json.loads(file.read())
        encrypted_message = RSA.encrypt_message(original_message_field.value, open_key)
        encrypted_message_field.value = ''.join(list(map(str, encrypted_message)))
        with open('encrypted_message.txt', 'w') as file:
            json.dump(encrypted_message, file)
        page.update()

    def decrypt_message(e):
        with open('close_key.txt', 'r') as file:
            close_key = json.load(file)
        with open('encrypted_message.txt', 'r') as file:
            encrypted_message = json.load(file)
        decrypted_message = RSA.decrypt_message(encrypted_message, close_key)
        decrypted_message_field.value = decrypted_message
        page.update()

    generate_keys_btn = ft.OutlinedButton(text='Generate Keys', width=150, height=50,
                                          on_click=generate_keys)
    encrypt_message_btn = ft.OutlinedButton(text='Encrypt message', width=300, height=50, on_click=encrypt_message)
    decrypt_message_btn = ft.OutlinedButton(text='Decrypt message', width=300, height=50, on_click=decrypt_message)
    open_key_field = ft.Text(value='Open key:', width=1000, disabled=True)
    close_key_filed = ft.Text(value='Close key:', width=1000, disabled=True)
    original_message_field = ft.TextField(label='Original message')
    encrypted_message_field = ft.Text(value='')
    decrypted_message_field = ft.Text(value='')
    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(value='RSA Encryptor/Decryptor', size=50),
                    ft.Row(
                        controls=[
                            generate_keys_btn,
                            ft.Column(
                                controls=[
                                    open_key_field,
                                    close_key_filed
                                ]
                            )
                        ]
                    ),
                    original_message_field,
                    encrypt_message_btn,
                    ft.Text(value='Encrypted text:', size=20),
                    encrypted_message_field,
                    decrypt_message_btn,
                    ft.Text(value='Decrypted text:', size=20),
                    decrypted_message_field
                ]
            ),
            alignment=ft.alignment.center
        )
    )
