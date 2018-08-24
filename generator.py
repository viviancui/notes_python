About generator

generator = (x*x for x in range(3))
for ele in generator:
    print(ele)

def create_generator():
    list = range(3)
    for ele in list:
        yield ele*ele

generator = create_generator()
for ele in generator:
    print(ele)



About next method
Think of it this way:
An iterator is just a fancy sounding term for an object that has a next() method.

generator = create_generator()
print generator will print an object

This is the next method
def square_numbers(list):
    for ele in list:
        yield (ele*ele)

numbers = square_numbers([1,2,3,4,5])
print next(numbers) #1
print next(numbers) #4
print next(numbers) #9
print next(numbers) #16
print next(numbers) #25
