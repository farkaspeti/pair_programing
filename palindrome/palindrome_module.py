def palindrome(str):
    bString = str.strip().lower().replace(" ","")
    cString = bString[::-1]
    if cString == bString:
        print("Its a Palindrome!")
        return True
    else:
        print("Its not a Palindrome")
        return False


def main():
    aString = input("What is your Word?: ")
    palindrome(aString)

    return


if __name__ == '__main__':
    main()
