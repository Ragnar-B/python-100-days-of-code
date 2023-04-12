# Python 100 Days of code

## Day 003

Tags: #Python #Logical-Operators 

### Control flow and logical operators

With a if or elif statement you can make choices in your code. You can use the else statement to run code if any of your choices aren't a match.

[[day03_exercise01.py]]
```python
number = int(input("Which number do you want to check? "))

result = number % 2

if result == 1:
    print("This is an odd number.")
else:
    print("This is an even number.")
```

Within the statement you can use operators like:

```
# Comparison Operators
>       greater than
<       smaller than
>=      greater than or equal to
<=      smaller than or equal to
==      equal to
!=      not equal to

# Logical Operators
and     if total <= 10 and total >= 90 -> both values need to pass.
or      if total <= 10 or total >= 90 -> either value much pass.
not     if not total == 10 -> This a negative, so anything but 10 is passed.

# Assignment Operators
+=      same as -> x = x + 3
-=      same as -> x = x - 3
*=      same as -> x = x * 3
/=      same as -> x = x / 3
%=      same as -> x = x % 3
//=     same as -> x = x // 3
**=     same as -> x = x ** 3
```
