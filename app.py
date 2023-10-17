
print("#34 Keyword Arguments")
def greet_user(first_name,last_name):
    print(f"Welcome {first_name} {last_name} !")
    # print("May I Help you!")


greet_user("Vinod","Deshmukh")
greet_user("Deshmukh","Vinod")
greet_user(last_name="Deshmukh",first_name="Vinod")
greet_user("Vinod",last_name="Deshmukh")

