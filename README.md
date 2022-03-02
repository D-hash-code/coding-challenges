# coding-challenges
keeping (trying to keep) my 🧠 sharp as a 🔪 


#Python

### Notes from Reverse Integer [leetcode 7] [link](python/reverse_integer.py)

The `int()` function and `//` division round down. So for any division that leads to `<0`, the output is larger in magnitude but still obviously considered 'rounding down'. Had to use math.trunc instead.

Pushing and popping is a handy method/approach when you want to reverse things without using much memory. More generally if you want to apply operations to each individual element of the data struct. Usually only strings, ints etc I suppose and not arrays. For arrays you can just use list comprehensions and maps? or are there benefits to push pop in arrays too?
