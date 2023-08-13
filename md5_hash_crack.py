# Author: George Maysack-Schlueter
import hashlib
from typing import TextIO

given_hash: str = input("Provide Md5 Hash to Crack --> ")
password_file: TextIO = open(r"C:\localFiles\wordlists\10-million-password-list-"
                             r"top-1000000.txt")
password_list: list[str] = password_file.read().split('\n')


def main():
    for word in password_list:
        guess = hashlib.md5(word.encode('utf-8')).hexdigest()
        if guess.upper() == given_hash or guess.lower() == given_hash:
            print('******************SUCCESS******************')
            print(f'[!] Pass: {word}')
            print(f'[#] Hash: {guess}')
            print('*******************************************\n')
            exit(0)
        else:
            print('-----------------INCORRECT-----------------')
            print(f'[-] Pass: {word}')
            print(f'[?] Guess: {guess}')
            print(f'[#] Given: {given_hash}')
            print('-------------------------------------------\n')
    print('[!] Password not found in wordlist...')


if __name__ == '__main__':
    main()
