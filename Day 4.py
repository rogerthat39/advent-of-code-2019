#Day 4 - 10/2/2020

#puzzle 1
def findNumPasswords(lowerLimit, upperLimit):
    possiblePasswords = []
    
    for i in range(lowerLimit, upperLimit):
        if(checkDigitsOnlyIncrease(i)):
            if(findAdjacentDouble(str(i))):
                possiblePasswords.append(i)

    return possiblePasswords

#returns true if each digit from left to right only increases in number (or stay the same)
def checkDigitsOnlyIncrease(num):
    previousDigit = 0
    for digit in str(num):
        #if current digit is less than previous, it breaks the rule
        if(int(digit) < previousDigit):
            return False
        else:
            previousDigit = int(digit)
    return True

#returns true if two adjacent digits are the same
def findAdjacentDouble(num):
    for i in range(0, len(num)-1):
        if(num[i] == num[i+1]):
            #extra check for puzzle 2
            if(numOfDigitsInPassword(num, num[i]) > 2):
                pass #continue looking for an adjacent pair
            else:
                return True
    return False

#returns how many of the given number there is in the password
def numOfDigitsInPassword(password, num):
    total = 0
    
    for digit in password:
        if(digit == num):
            total += 1
            
    return total

print(len(findNumPasswords(128392, 643281)))
