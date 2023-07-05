print("Welcome To The Game!")

#ask users if they want to play the game
playing = input('\n Do you want to play? ').lower()
print(playing)

if playing != "yes":
    quit()

print('Okay! \n Lets play :)')

#Questions
answer = input('\n What does CPU stand for? ')
if answer.lower() == 'central processing unit':
    print('correct!')
else:
    print('Incorrect! :(')

answer = input('\n What does GPU stand for? ').lower()
if answer == 'graphics processing unit':
    print('correct!')
else:
    print('Incorrect! :(')

answer = input('\n What does RAM stand for?  ')
if answer.lower() == 'random access memory':
    print('correct!')
else:
    print('Incorrect! :(')


answer = input('\n What does PSU stand for? ')
if answer.lower() == 'power supply':
    print('correct!')
else:
    print('Incorrect! :()')

#answer = input('\n  ')
#if answer == ' ':
#    print('correct!')
#else:
#    print('Incorrect! :()')

