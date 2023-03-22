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


def main():
    menu()
    choice = int(input('Please enter an option: '))
    if choice == 1:
        password = input('Please enter your password to encode: ')
        password = [int(i) for i in password]
        encode(password)
        print('Your password has been encoded and stored!')


if __name__ == "__main__":
    while True:
        main()
        print()
        
