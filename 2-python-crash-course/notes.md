# 2. Chapter - Python Crash Course

- `sorted(x, key?=function, reverse=True)` -> does not change x
- randomness `import random; random.seed(10); random.random(); random.randrage(10); random.randrange(3, 6), random.shuffle(range(10))`

## Regular Expressions

```python
import re

print all([
    not re.match("a", "cat"), # Cat does not start with a
    re.search("a", "cat"), # cat contains a
    3 == len(re.split("[ab]", "carbs")), # split on a or b
    "R-D-" == re.sub("[0-9]", "-", "R2D2") # replace digits
])

```
