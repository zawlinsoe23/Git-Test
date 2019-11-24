5.4. Sets

>>> basket = {'apple', 'orange', 'apple', 'orange', 'banana'}
>>> print(basket)
{'banana', 'orange', 'apple'}
>>> basket = {'banana', 'apple', 'cucumber', 'pineaoole', 'orange', 'grape', }
>>> basket = {'banana', 'apple', 'cucumber', 'pineaoole', 'orange', 'grape', 'apple', 'banana'}
>>> print(basket)
{'apple', 'pineaoole', 'cucumber', 'grape', 'orange', 'banana'}
>>> print (basket)
{'apple', 'pineaoole', 'cucumber', 'grape', 'orange', 'banana'}
>>> 'orange' in basket
True
>>> 'crabgrass' in basket
False



>>> # Demonstrate set operations on unique letters from two words
...
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
>>> a - b                              # letters in a but not in b
{'r', 'd', 'b'}
>>> a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # letters in both a and b
{'a', 'c'}
>>> a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}

>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'r', 'd'}