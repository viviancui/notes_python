About list comprehension
The difference between list comprehension and generator is just () vs []

list = range(3)
squares = [x*x for x in list]
print squares

-----------------------
Generator
generator = (x*x for x in range(3))
for ele in generator:
    print(ele)
