from random import choice


keys = '0123456789'
m = input('099 or 098 or 091 or 090 --> ')

for i in range(1000):

    p = str(m) + choice(keys) + choice(keys) + choice(keys) + choice(keys) + choice(keys) + choice(keys) + choice(keys) + choice(keys)
    print(p)
input('press key to exit /')