# project 55

def isLychrel(number):
    for i in range(50):
        number = number + reverse(number)


        if (isPalindrome(number)):
            return False
    return True


def isPalindrome(number):
    return number == reverse(number)


def reverse(number):
    reverse = 0
    while (number > 0):
        remainder = number % 10
        reverse = (reverse * 10) + remainder
        number = int(number / 10)

    return reverse


count = 0
for i in  range(10000):
    if isLychrel(i):
        count+=1
print(count)