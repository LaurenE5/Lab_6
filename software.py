def menu():
    print('Menu')
    print('------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print()
    return


def encode(password):
    new_password = [element + 3 for element in password if element == element]
    return new_password


def decode(new_password):
    password = [element - 3 for element in new_password]
    return password


def main():
    while True:
        menu()
        choice = int(input('Please enter an option: '))
        if choice == 1:
            password = input('Please enter your password to encode: ')
            password = [int(i) for i in password]
            encode(password)
            print('Your password has been encoded and stored!')
        if choice == 2:
            new_password = encode(password)
            password = decode(new_password)
            new_password = ''.join(str(i) for i in encode(password))
            password = ''.join(str(i) for i in password)
            print(f'The new password is {new_password}, and the original password is {password}.')
            print()
        if choice == 3:
            exit()


if __name__ == "__main__":
    while True:
        main()
        print()
        
