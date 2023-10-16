print("#30 Dictionaries: Write a program which returns phone number into words")
ph_number={
    "0":"Zero",
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"four",
    "5":"five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9":"Nine"
}
numbers=input("Phone:")
output=""
for number in numbers:
    output+=ph_number.get(number,"!")+ " "
print(output)


