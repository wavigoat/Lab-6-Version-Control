'''
Lab 6
Authors: Kaitlyn Tran and Abby Zheng
Class: COP3502C
Section: 12309
Description: A password encoder that shifts each digit up by 3.
'''
# Original Coder: Kaitlyn Tran

def encode(decoded):
    # Encode Function
    encoder = ''
    for i in decoded:
        encoded_digit = str(int(i) + 3)
        encoder += encoded_digit
    return encoder


if __name__ == '__main__':
    while True:
        # Menu
        print('Menu\n'
              '-------------\n'
              '1. Encode\n'
              '2. Decode\n'
              '3. Quit')
        option = int(input('Please enter an option: '))

        # Options
        if option == 1:
            password = input('Please enter your password to encode: ')
            encoded_password = encode(password)
            print('Your password has been encoded and stored!')
        elif option == 2:
            # Decode Function is used here - partner codes this
            decoded_password = decode(encoded_password)
            print(f'The encoded password is {encoded_password}, and the original password is {decoded_password}.')
        else:
            break
