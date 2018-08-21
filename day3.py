"""print(bool([]))
data=[]
if data:
    process(data)
else:
    print("there is no data")
    
for n in range(10):
    if n%2==0:
        print("Even",n)
    continue
print("odd",n)
    
"""

def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
        return True
n=input("Enter a number")
for x in range(2, int(n)):
        if is_prime(x):
            print(x,"is prime")
        else :
            print(x,"is not prime")
