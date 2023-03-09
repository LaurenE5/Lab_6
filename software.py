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
    print(new_password)
    return new_password


def main():
    menu()
    choice = int(input('Please enter an option: '))
    if choice == 1:
        password = input('Please enter your password to encode: ')
        password = [int(i) for i in password]
        encode(password)
        print('Your password has been encoded and stored!')

    '''
    if choice == 2:
        new_password = encode(password)
        [(i, end="") for i in new_password]
        print(f'The encoded password is {new_password}, and the original password is {password}')
    else:
        exit()
    '''


if __name__ == "__main__":
    main()
