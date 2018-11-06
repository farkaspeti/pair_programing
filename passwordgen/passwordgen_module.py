import string 
from random import *

def passwordgen():
    minChar = 8
    maxChar = 16
    allChar = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(allChar) for x in range(randint(minChar, maxChar)))
    print("This is your password: ", password)
    return password


def main():
    passwordgen()
    return


if __name__ == '__main__':
    main()
