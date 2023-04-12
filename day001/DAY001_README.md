# Python 100 Days of code

## Day 001

Tags: #Python #Variables #Functions

### Variables and Basic Functions

user is the variable. 

input() is a function which can be used to have an user input data. Datatype of the input is a string.

Print() function can be used to output the data.

`\n` will generate a new line.

### [[print-input.py]] 
```python
user = input("Who are you?\n")
print("The user is: " + user)
```
---

Variables can we overritten when running the code.
### [[var.py]]
```python
name = "Jack"
print(name)

name = "Angela"
print(name)
```
---

len() function can we used to get to number of characters in a string.
### [[len.py]]
```python
name = input("What is your name?")
length = len(name)
print(length)
```
---

Final excerise was to create a bandname generator, which combines 2 variables into one string and Output this.
### [[band-name-generator.py]]
```python
#1. Create a greeting for your program.
print("Hi there!")
#2. Ask the user for the city that they grew up in.
city = input("In which city did you grew up?\n")
#3. Ask the user for the name of a pet.
pet = input("Whats the name of your pet?\n")
#4. Combine the name of their city and pet and show them their band name.
print(city + " " + pet)
#5. Make sure the input cursor shows on a new line:
```