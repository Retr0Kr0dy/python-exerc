import random
for z in range(0, 50):
    x = random.randrange(0, 100)
    if x % 3 == 0 and x % 5 == 0:
        print(x, " FizzBuzz")
    elif x % 3 == 0:
        print(x," Fizz")
    elif x % 5 == 0:
        print(x, " Buzz")
    else:
        print(x)