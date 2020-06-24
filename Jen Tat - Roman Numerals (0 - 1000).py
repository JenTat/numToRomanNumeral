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

def hundreds(num):
    hundredsPlace = int(str(num)[0])
    if hundredsPlace == 1:
        multiplier = 1
    elif hundredsPlace == 2:
        multiplier = 2
    else:
        multiplier = 3
    change = num - (100*multiplier)
    difference = main(change)
    return ("C"*multiplier) + difference

def fourHundreds(num):
    change = num - 400
    difference = main(change)
    return "CD" + difference

def overMonkey(num):
    hundredsPlace = int(str(num)[0])
    amount = hundredsPlace - 5
    change = num - hundredsPlace*100
    difference = main(change)
    return "D" + "C"*amount + difference

def nineHundreds(num):
    change = num - 900
    change = main(change)
    return "CM" + change

def main(num):
    if num < 5:
        numeral = underFive(num)
    elif num > 4 and num < 10:
        numeral = underTen(num)
    elif num > 9 and num < 40:
        numeral = underForty(num)
    elif num > 39 and num < 50:
        numeral = forties(num)
    elif num > 49 and num < 60:
        numeral = fifties(num)
    elif num > 59 and num < 90:
        numeral = underNinety(num)
    elif num > 89 and num < 100:
        numeral = nineties(num)
    elif num > 99 and num < 400:
        numeral = hundreds(num)
    elif num > 399 and num < 500:
        numeral = fourHundreds(num)
    elif num > 499 and num < 900:
        numeral = overMonkey(num)
    elif num > 899 and num < 1000:
        numeral = nineHundreds(num)
    elif num == 1000:
        numeral = "M"
    return numeral

userCont = input("To exit type 'END': \n")
while userCont.lower() != "end":
    num = input("Please enter the number you want written in Roman numerals.\n")
    while num.isnumeric() == False or int(num) > 1000:
        print("Please enter an integer value below 1000.")
        num = input("Please enter the number you want written in Roman numerals.\n")
    num = int(num)
    if num == 0:
        final = "There is no Roman numeral for zero."
    else:
        final = main(num)
    print("Modern number: " + str(num))
    print("Roman numeral: " + str(final))
    userCont = input("To exit type 'END': \n")
print("The program has ended.")
