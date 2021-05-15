# First Approach using built-in library, itertools.
from itertools import chain, combinations

def powerset(iterable):
    # powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

list(powerset("abcd")) 



# Second Approach with scratch. 
def powerset(s):
    x = len(s)
    powers = [1 << i for i in range(x)]
    for i in range(1 << x):
        yield [a for power, a in zip(powers, s) if i & power]
        
print(list(powerset([4, 5, 6])))
