print("#27 Lists Methods: Write a Program to remove the duplicates on a List")
numbers=[10,21,23,21,10,10,5,44]
uniques=[]
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(numbers)
print(uniques)