import random


def current_rating(ratings, name):
    for line in ratings:
        if line.find(name + ' ') != -1:
            return int(line[:-1].lstrip(name + ' '))
    return 0


def simulate_game(user_choice, computer_choice):
    # Sort in winning order. Each option can win 7 next options
    variants = ['rock', 'fire', 'scissors', 'snake', 'human', 'tree',
                'wolf', 'sponge', 'paper', 'air', 'water', 'dragon',
                'devil', 'lightning', 'gun']

    user_index = variants.index(user_choice)
    computer_index = variants.index(computer_choice)

    if user_index == computer_index:
        print('There is a draw ({})'.format(computer_choice))
        return 50
    elif user_index + 7 >= 15:
        if user_index < computer_index or (user_index + 7) % 15 >= computer_index:
            print('Well done. The computer chose {} and failed'.format(computer_choice))
            return 100
        else:
            print('Sorry, but the computer chose {}'.format(computer_choice))
            return 0
    else:
        if user_index < computer_index <= user_index + 7:
            print('Well done. The computer chose {} and failed'.format(computer_choice))
            return 100
        else:
            print('Sorry, but the computer chose {}'.format(computer_choice))
            return 0


name = input('Enter your name: ')
print('Hello, ' + name)

file = open('rating.txt', 'r')
data = file.readlines()
rating = current_rating(data, name)


options = input().split(',')
print(options)
if options == ['']:
    options = ['scissors', 'paper', 'rock']
print("Okay, let's start")

while True:
    user = input()

    if user == '!exit':
        print('Bye!')
        break

    if user == '!rating':
        print('Your rating: ' + str(rating))
        continue

    if user not in options:
        print('Invalid input')
        continue

    computer = random.choice(options)

    rating += simulate_game(user, computer)
