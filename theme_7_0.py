import random
num = random.randint(1, 100)
for i in range(10):
    user = int(input('Ну что? Какое число я загадал? '))
    if user < num:
        print('Больше')
    elif user > num:
        print('Меньше')
    else:
        print('Угадал! и потратил всего %s попыток' % (i + 1))
        break
    if i == 9:
        print('Вы исчерпали все попытки и не угадали! А жаль')