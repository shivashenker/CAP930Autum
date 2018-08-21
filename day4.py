"""print(isinstance(4, object))
print(isinstance("Hello", object))
print(isinstance(None, object))
print(isinstance([1,2,3], object))

print((4).__sizeof__())
def compute(a,b,c):
    return(a+b)*c
'print(compute(10,12,13))'
'print(compute([1],[2,3],2))'
print(compute('l','olo',4))
print(1==2.0)
print(type(1)!=type(1.0))
print(int!=float)

greeting= "Hai hello how are you"
print(greeting[4])
print('you' in greeting)
print(greeting.find('ou'))
print(greeting.replace('ou','y'))
print(greeting.startswith('Hai'))
print(greeting.isalpha())
print(greeting.lower())
print(greeting.title())
print(greeting.strip())
print(greeting.strip('you'))

print("Ram and shyam are god".split())
print("03-03-2016".split(sep='-'))
print(','.join(['raghav','rohit','revanth']))"""

print('{} {}'.format('monty','python'))
print("{0} can be {1} {0}s".format("strings","formatted"))
print("{name} loves {food}".format(name="sam",food="plums"))
