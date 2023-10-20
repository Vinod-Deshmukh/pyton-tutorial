import random

print("#44 Generating Random Number")


class Dice:
    def roll(self):
        roll1=random.randint(1,6)
        roll2=random.randint(1,6)
        # result=(roll1,roll2)
        # return result
        return roll1,roll2


dice=Dice()
print(dice.roll())