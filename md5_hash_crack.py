import hashlib
given_hash = input("Provide Md5 Hash to Crack --> ")
password_file = open("/home/george/password_lists/10-million-password-list-top-1000000.txt", "r")
password_list = password_file.read().split('\n')
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