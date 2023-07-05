print("Welcome To The Game!")

#ask users if they want to play the game
playing = input('\n Do you want to play? ').lower()
print(playing)

if playing != "yes":
    quit()

print('Okay! \n Lets play :)')
score = 0
#Questions
answer = input('\n What does CPU stand for? ')
if answer.lower() == 'central processing unit':
    print('correct!')
    score += 1
else:
    print('Incorrect! :(')

answer = input('\n What does GPU stand for? ').lower()
if answer == 'graphics processing unit':
    print('correct!')
    score += 1
else:
    print('Incorrect! :(')

answer = input('\n What does RAM stand for?  ')
if answer.lower() == 'random access memory':
    print('correct!')
    score += 1
else:
    print('Incorrect! :(')


answer = input('\n What does PSU stand for? ')
if answer.lower() == 'power supply':
    print('correct!')
    score += 1
else:
    print('Incorrect! :()')

print('You Got ' + str(score) + " Questions Correct!")
#answer = input('\n  ')
#if answer == ' ':
#    print('correct!')
#else:
#    print('Incorrect! :()')

