# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
number_ppl = len(names) - 1
random_ppl = random.randint(0 , number_ppl)
bill = names[random_ppl]

print(bill + " is going to buy the meal today!")