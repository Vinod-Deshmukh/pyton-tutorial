print("#21 Car Game!")
command = ""

while True:
    command = input(">").lower()
    if command == 'help':
         print('start- to start the car \nstop- to stop the car \nquit-to exit')
    elif command == 'start':
        print('Car started.... Ready to go!')
    elif command == 'stop':
        print('Car stopped.')
    elif command == 'quit':
        break
    else:
        print('I don''t understand')



