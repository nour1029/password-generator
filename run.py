import random
import string

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'


def generate():
    loop = True
    while loop:
        x = []
        for _ in range(random.randint(8, 14)):
            x.append(random.choice(letters))
        if '_' in x:
            for i in x:
                if i in '0123456789':
                    loop = False

    return ''.join(x)


print(generate())
