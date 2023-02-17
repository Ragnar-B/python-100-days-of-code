# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lowercase_name1 = name1.lower()
lowercase_name2 = name2.lower()

t = lowercase_name1.count("t") + lowercase_name2.count("t")
r = lowercase_name1.count("r") + lowercase_name2.count("r")
u = lowercase_name1.count("u") + lowercase_name2.count("u")
e = lowercase_name1.count("e") + lowercase_name2.count("e")
l = lowercase_name1.count("l") + lowercase_name2.count("l")
o = lowercase_name1.count("o") + lowercase_name2.count("o")
v = lowercase_name1.count("v") + lowercase_name2.count("v")

total_true = t + r + u + e
total_love = l + o + v + e
total = (total_true * 10) + total_love

# print(total)
# print(type(total))

if total <= 10 or total >= 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total >= 40 and total <= 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")