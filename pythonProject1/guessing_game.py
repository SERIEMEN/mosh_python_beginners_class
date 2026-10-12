secret_number = 7
guess_count = 0 #no of guesses to be made
guess_limit = 3
# use meaningful and descriptive name to use as your variable name
# a while statement can also have an else part can it also have an elif part?

# while condition:
while guess_count < guess_limit:
    guess =int(input('Guess: '))
    guess_count +=1
    if guess == secret_number:
        print('You won!')
        break
else:
    print('YOU FAILED!')

# dry do not repeat code
entry = ""
while entry.lower() != 'quit':
    entry = input('> ').lower()
    if entry =='start':
        print('Car Started')
    elif entry == 'stop':
        print('car stopped')
    elif entry == 'help':
        print("""
start - to start the car
stop - to stop the car
quit  to quit""")
    elif entry == 'quit':
        break
    else:
        print('Sorry, I do not understand this')

entry = ""
started = False
while True:
    entry = input('> ').lower()
    if entry =='start':
        if started:
            print('Car is already started!')
        else:
            started = True
        print('Car Started')
    elif entry == 'stop':
        if not started:
            print('Car is already stopped!!')
        else:
            started = False
        print('car stopped')
    elif entry == 'help':
        print("""
start - to start the car
stop - to stop the car
quit  to quit""")
    elif entry == 'quit':
        break
    else:
        print('Sorry, I do not understand this')


''' entry = input('> ')
entry_count = str(5)
while entry < entry_count:
    entry = str(input('> '))
    entry_count += 1
    if entry := 'start':
            print('Car started...Ready to go!')
    elif entry := 'stop':
            print('Car stopped.')
    elif entry := 'help':
            print('start - to start the car'
        'stop - to stop the car'
        'quit - to quit the car')
    elif entry := 'quit':
        print()
        break
else:
    print('I do not understand') '''