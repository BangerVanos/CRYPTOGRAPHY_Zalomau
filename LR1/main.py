from src.password_generator import PasswordGenerator
import random

if __name__ == '__main__':
    password = PasswordGenerator.generate_password(random.randint(8, 20))
    print(f'Your random password is: {password}')
    PasswordGenerator.show_frequency_distribution(password)
    print(f'Average time of cracking 3-symbol password (10 times) is '
          f'{PasswordGenerator.average_crack_time(PasswordGenerator.generate_password(3), 10)}')
    PasswordGenerator.average_crack_time_plot(2, 4, 5)
