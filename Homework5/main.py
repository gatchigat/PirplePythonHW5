def primeNo(x):
    return x in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


for counter in range(1, 101):
    num = ''
    if primeNo(counter):
        num = 'Prime'
    if counter % 3 == 0:
        num = 'Fizz'
    if counter % 5 == 0:
        num = 'Buzz'
    if (counter % 3 == 0) and (counter % 5 == 0):
        num = 'FizzBuzz'
    print(num if str(num) else(counter))
