# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet(name):
  print(f"Hi {name}")
  print("Hello")
  print("World")

greet("Machiel")

# Functions with more than 1 input

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with(location="Amsterdam", name="Machiel")