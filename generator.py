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
