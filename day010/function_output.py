#Function
def function01():
    print("Hello World!")

#Function Input
def function02(text):
    print(text)

#Function Output
def function03():
    result = 3 * 2
    return result

#Functions with outputs

def format_name(f_name, l_name):
    """This is a docstring used for explaining the function"""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    first = f_name.title()
    last = l_name.title()
    
    return f"{first} {last}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))

