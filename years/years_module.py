import datetime


def years(age):

    date = datetime.datetime.now()
    currentYear = date.year
    agesToHundred = 100 - age
    yearWhenHundred = currentYear + agesToHundred

    return yearWhenHundred


def main():
    aString = input("What is your name?")
    bInt = int(input("What is your age?"))
    cInt = int(input("How many times do you want to print the year, when you will turn hundred years old?"))
    
    yearWhenHundred = years(bInt)
    for i in range(cInt):
        print(aString,", You will turn 100 in the year of: ",yearWhenHundred)
    
    return


if __name__ == '__main__':
    main()
