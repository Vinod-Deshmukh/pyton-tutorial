print("#21 Car Game!")
command = ""
started=False
while True:
    command = input(">").lower()
    if command == 'help':
         print('start- to start the car \nstop- to stop the car \nquit-to exit')
    elif command == 'start':
        if started:
            print("car is already started.")
        else:
            started = True
            print('Car started.')
    elif command == 'stop':
        if not started:
            print("car is already stopped")
        else:
            started=False
            print('Car stopped.')
    elif command == 'quit':
        break
    else:
        print('I don''t understand')



