# Python 100 Days of code

## Day 004

Tags: #Python #Lists #Nested-Lists #Functions 

### Lists

```python
fruit = ["apple","pear","banana"]
print(fruit[0])
# This will print apple

print(fruit[1])
# This will print pear

print(fruit[-1])
# This will print banana

fruit.append("strawberry")
# This will append strawberry to the list.
```
### Nested lists

```python
list1 = ["apple","pear"]
list2 = ["banana","strawberry"]
nested_list = [list1, list2]

print(nested_list)
# This will print [['apple', 'pear'], ['banana', 'strawberry']]

print(nested_list[1])
# This will print ['banana', 'strawberry']

print(nested_list[1][0])
# This will print banana
```

### Randomisation

```python
import random

random.randint(1,100)
# This will generate a random integer from 1 - 100 including 100

random.random()
# This will generate a random float between 0 and 1, not including 1
```