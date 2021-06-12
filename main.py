from random import randrange
test_string = ['a','b','c','d','e']
random_string = ''
for i in test_string:
  counter = randrange(len(test_string))
  random_string += test_string[counter]
print(random_string)