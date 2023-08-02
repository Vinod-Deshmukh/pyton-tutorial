print("Weight Converter Program")
weight=float(input("Weight: "))
unit=input("(L)bs or (K)g: ")
if unit=="l" or unit=="L":
    weight=weight*0.45
    print(f'You are {weight} Kgs')
else:
    weight=weight/0.45
    print(f'You are {weight} pounds')

