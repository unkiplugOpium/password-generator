import random 


simbols =  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
long_p = int(input('puneti parola cu lungimea dumneavoastra  '))
password = ''
for simbol in range(long_p):
    password+= random.choice(simbols)
print(password)
0


