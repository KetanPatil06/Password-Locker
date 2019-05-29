import pyperclip

passwords = {'Facebook': 'xxxx', 'Instagram': 'xxxxxx', 'Youtube': 'xxxxxxx'}

tries = 0
tries_remaining = 3
pass_len = len(passwords)


def ask():
    mast_pass = 'HailHydra'
    ask_mast_pass = input('Please enter the master password: ')
    if ask_mast_pass == mast_pass:
        print(f"{pass_len} found.")
        for x in passwords.keys():
            print(x)

        which_pass = input('Type the name of the password title you are looking for: ')
        paswd = passwords[which_pass]
        pyperclip.copy(paswd)
        print('Password Copied to clipboard.')

        exit()
    else:
        print('Incorrect Password, Please Try again')


while tries < tries_remaining:
    tries += 1
    ask()
    print(f"{3 - tries} tries remaining")


print('***Do not try to breach the system***')
