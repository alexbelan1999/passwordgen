import random

symbols = '_()+-/*!&$#?=@<>'
lowercase = 'abcdefghijklnopqrstuvwxyz'
uppercase = lowercase.upper()
numbers = '1234567890'

number = 0
while number < 1:
    number = int(input('Количество паролей: '))

length = 0
while length < 4:
    length = int(input('Длина пароля: '))

for n in range(number):
    password = ''
    flag1 = True
    flag2 = True
    flag3 = True
    flag4 = True

    for i in range(length):
        if 0 <= i <= 3:
            while flag1 or flag2 or flag3 or flag4:
                choice = random.choice([0, 1, 2, 3])
                if choice == 0 and flag1:
                    password += random.choice(symbols)
                    flag1 = False
                    break

                elif choice == 1 and flag2:
                    password += random.choice(uppercase)
                    flag2 = False
                    break

                elif choice == 2 and flag3:
                    password += random.choice(lowercase)
                    flag3 = False
                    break

                elif choice == 3 and flag4:
                    password += random.choice(numbers)
                    flag4 = False
                    break

        else:
            choice = random.choice([0, 1, 2, 3])
            if choice == 0:
                password += random.choice(symbols)

            elif choice == 1:
                password += random.choice(uppercase)

            elif choice == 2:
                password += random.choice(lowercase)

            elif choice == 3:
                password += random.choice(numbers)

    print(f'Пароль [{n + 1}]: {password}')
