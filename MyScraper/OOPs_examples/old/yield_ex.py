# Python Yeild Keyword Example

# Write a program to create a generator that generates cubes of numbers up to 1000 using Yield


def generator_fun():
    i = 1
    while True:
        yield i*i*i
        i+=1

generator_fun.__doc__ = "Cube generator"

for i in generator_fun():
    if(i>100):
        break
    print(i)
