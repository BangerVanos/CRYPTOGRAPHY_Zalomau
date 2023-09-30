import dearpygui.dearpygui as dpg
from src.image_encryption import ImageEncrypter
import random


class App:
    def __init__(self, window_w: int = 1280, window_h: int = 720):
        self.window_h = window_h
        self.window_w = window_w
        self.dialog_filters = ['.jpeg', '.jpg', '.png']
        self.__image_path: str = ''
        self.__aes_key_length = (16, 24, 32)
        self.__des_key_length = (8,)

    def run(self):
        dpg.create_context()
        dpg.create_viewport(title='Image encryption app', width=self.window_w, height=self.window_h)
        dpg.setup_dearpygui()

        self.__main_window()
        dpg.set_primary_window('main_window', True)

        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()

    def __main_window(self):
        with dpg.file_dialog(tag='image_dialog', width=640, height=480, show=False,
                             callback=self.__load_image):
            dpg.add_file_extension('Image files{.jpg,.png,.jpeg}')
            dpg.add_file_extension('.jpeg')
            dpg.add_file_extension('.jpg')
            dpg.add_file_extension('.png')

        with dpg.window(label='Encrypt your image', width=self.window_w, height=self.window_h,
                        no_move=True, no_collapse=True, no_close=True, tag='main_window') as main_window:
            self.__main_window = main_window
            with dpg.table():
                dpg.add_table_column(label='Choose encryption algorithm')
                dpg.add_table_column(label='Choose encryption mode')
                dpg.add_table_column(label='Enter encryption key')
                with dpg.table_row():
                    dpg.add_radio_button(tag='algorithm', items=['AES', 'DES'], default_value='AES',
                                         callback=self.__generate_key)
                    dpg.add_radio_button(tag='mode', items=['ECB', 'CBC', 'CFB', 'OFB', 'CTR'], default_value='ECB')
                    dpg.add_input_text(tag='key', default_value='0000000000000000')
            with dpg.table():
                dpg.add_table_column(label='')
                dpg.add_table_column(label='')
                with dpg.table_row():
                    dpg.add_button(callback=self.__show_image_dialog, label='Choose image')
                    dpg.add_table_cell(tag='original_image_container')
                with dpg.table_row():
                    dpg.add_button(label='Encrypt', callback=self.__encrypt_image)
                    dpg.add_table_cell(tag='encrypted_image_container')

    @staticmethod
    def __show_image_dialog():
        dpg.show_item('image_dialog')

    def __load_image(self, sender, app_data, user_data):
        img_path = app_data['file_path_name']
        self.__image_path = img_path
        width, height, channels, img_data = dpg.load_image(img_path)
        if dpg.does_alias_exist('original_image_texture'):
            dpg.delete_item('original_image')
            dpg.remove_alias('original_image_texture')
        with dpg.texture_registry(show=False):
            dpg.add_static_texture(width=min(width, 640), height=min(height, 480), default_value=img_data,
                                   tag='original_image_texture')
        dpg.add_image('original_image_texture', parent='original_image_container', tag='original_image')

    def __encrypt_image(self):
        if self.__image_path is None or self.__image_path == '':
            return
        if dpg.get_value('algorithm') == 'AES' and len(dpg.get_value('key')) not in self.__aes_key_length:
            return None
        elif dpg.get_value('algorithm') == 'DES' and len(dpg.get_value('key')) not in self.__des_key_length:
            return None
        ImageEncrypter.encrypt_image(self.__image_path, dpg.get_value('key'),
                                     dpg.get_value('algorithm'), dpg.get_value('mode'))
        width, height, channels, img_data = dpg.load_image('images/encrypted.jpg')
        if dpg.does_alias_exist('encrypted_image_texture'):
            dpg.delete_item('encrypted_image')
            dpg.remove_alias('encrypted_image_texture')
        with dpg.texture_registry(show=False):
            dpg.add_static_texture(width=min(width, 640), height=min(height, 480), default_value=img_data,
                                   tag='encrypted_image_texture')
        dpg.add_image('encrypted_image_texture', parent='encrypted_image_container', tag='encrypted_image')

    @staticmethod
    def __generate_key():
        digits = '0123456789'
        key_sym_amount = 16 if dpg.get_value('algorithm') == 'AES' else 8
        dpg.set_value('key', int(''.join([random.choice(digits) for _ in range(key_sym_amount)])))
