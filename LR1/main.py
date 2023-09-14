from src.password_generator import PasswordGenerator


if __name__ == '__main__':
    password = PasswordGenerator.generate_password(int(input("Enter password length: ")))
    print(f'Your random password is: {password}')
    PasswordGenerator.show_frequency_distribution(password)
    print(f'Average time of cracking 3-symbol password (10 times) is '
          f'{PasswordGenerator.average_crack_time(PasswordGenerator.generate_password(3), 10)}')
    PasswordGenerator.average_crack_time_plot(2, 4, 5)
