import random, time

z = ["c","a","E","D","s","Y","O","K","j",";",",l","h","u","gy"]
i = random.choice(z)
l = ['\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[1;35m', '\033[36m']
while True:
    nnn=random.randrange(300, 500)
    while len(i) <= nnn:
        x = random.choice(l)
        y = random.choice(z)
        print (''.join(x+i))
        time.sleep(0.01)
        i += x+y
    mmm=random.randrange(10, 200)
    while len(i) >= mmm:
        x = random.choice(l)
        y = random.choice(z)
        time.sleep(0.001)
        print(x+i)
        i = i[:-1]
