# project 17

from num2words import num2words # num2words - Convert numbers to words in multiple languages


def number_letter_counts(num):
    result = 0
    for i in range(1,num+1):
        result+=(len(''.join(''.join(num2words(i).split('-')).split(' '))))
    return result
    
print(number_letter_counts(1000))
