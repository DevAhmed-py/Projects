#FizzBuzzPrime

for i in range(1,20):

    if i%3 == 0 and i%5 == 0:
        print('FizzBuzz')
    
    elif i%3 == 0:
        print('Fizz')

    elif i%5 == 0:
        print('Buzz')

    elif i%i == 0 and i%2 == 1 and i>1:
        print('Prime')

    else:
        print(i)
