print("#37 Exception")
try:
    age = int(input('Age: '))
    print(age/0)
except ValueError:
    print("Invalid Value")
except ZeroDivisionError:
    print("Invalid Division")

