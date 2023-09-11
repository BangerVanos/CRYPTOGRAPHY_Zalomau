import random
import time

import matplotlib.pyplot as plt


class PasswordGenerator:
    SYMBOLS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    @classmethod
    def generate_password(cls, password_length: int) -> str:
        """Генерирует строку из символов алфавита и цифр с заданной длиной."""
        return ''.join([random.choice(cls.SYMBOLS) for _ in range(password_length)])

    @classmethod
    def show_frequency_distribution(cls, password: str) -> None:
        """Визуализирует частотное распределение символов в строке."""
        unique_symbols = set(list(password))
        plot_values = {symbol: password.count(symbol) for symbol in unique_symbols}
        plt.bar(plot_values.keys(), plot_values.values())
        plt.show()

    @classmethod
    def __crack_password_time(cls, password: str) -> float:
        """Время взлома пароля"""
        start_time = time.time()
        while True:
            if cls.generate_password(len(password)) == password:
                break
        end_time = time.time()
        return end_time - start_time

    @classmethod
    def average_crack_time(cls, password: str, num_of_tries: int) -> float:
        """Вычисление среднего времени подбора пароля"""
        all_tries_time = sum([cls.__crack_password_time(password) for _ in range(num_of_tries)])
        return all_tries_time / num_of_tries

    @classmethod
    def average_crack_time_plot(cls, min_length: int = 8, max_length: int = 20, num_of_tries: int = 10):
        """График зависимости среднего времени взлома пароля от его длины"""
        average_crack_times = {}
        for i in range(min_length, max_length + 1):
            generated_password = cls.generate_password(i)
            average_crack_times[i] = cls.average_crack_time(generated_password, num_of_tries)
        plt.plot(average_crack_times.keys(), average_crack_times.values())
        plt.show()
