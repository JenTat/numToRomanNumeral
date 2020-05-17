def underFive(num):
    if num == 4:
        return "IV"
    else:
        return "I" * num    

def underTen(num):
    if num == 5:
        return "V"
    elif num == 9:
        return "IX"
    else:
        return "V" + ("I" * (num - 5))

def underForty(num):
    change = num % 10
    if change < 5:
        change = underFive(change)
    else:
        change = underTen(change)
    return "X" * (num//10) + change

def forties(num):
    change = num - 40
    if change < 5:
        change = underFive(change)
    else:
        change = underTen(change)
    return "XL" + change

def fifties(num):
    change = num - 50
    if change < 5:
        change = underFive(change)
    else:
        change = underTen(change)
    return "L" + change

def underNinety(num):
    tens = num - 60
    tens = underForty(tens)
    return "LX" + tens

def nineties(num):
    change = num - 90
    if change < 5:
        change = underFive(change)
    else:
        change = underTen(change)
    return "XC" + change   

def main():
    if num == 0:
        print("There is no Roman numeral for zero.")
    elif num < 5:
        print("Modern number: " + str(num))
        print("Roman numeral: " + underFive(num))
    elif num > 4 and num < 10:
        print("Modern number: " + str(num))
        print("Roman numeral: " + underTen(num))
    elif num > 9 and num < 40:
        print("Modern number: " + str(num))
        print("Roman numeral: " + underForty(num))
    elif num > 39 and num < 50:
        print("Modern number: " + str(num))
        print("Roman numeral: " + forties(num))
    elif num > 49 and num < 60:
        print("Modern number: " + str(num))
        print("Roman numeral: " + fifties(num))
    elif num > 59 and num < 90:
        print("Modern number: " + str(num))
        print("Roman numeral: " + underNinety(num))
    elif num > 89 and num < 100:
        print("Modern number: " + str(num))
        print("Roman numeral: " + nineties(num))
    elif num == 100:
        print("Modern number: " + str(num))
        print("Roman numeral: C")

userCont = input("To exit enter 'END': ")
while userCont.lower() != "\'end\'":
    num = input("Please enter the number you want written in Roman numerals.\n")
    while num.isnumeric() == False and int(num) > 100:
        print("Please enter an integer value below 100.")
        num = input("Please enter the number you want written in Roman numerals.\n")
    num = int(num)
    main()
    userCont = input("To exit enter 'END'.")
