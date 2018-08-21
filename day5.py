"""RollNo=[1,2,3,4,5,6,5,6,56,5,36,5,8,6,9]
for i in range(1,60):
    RollNo.append(i)

RollNo.sort()
print(RollNo)


empty={}
print(type(empty))
print(empty==dict())

a=dict(one=1, two=2, three=3)
b={"one":1, "two":2, "three":3}
print(a==b)
"""
Me=dict(name='vara', lastname='prasad', age=25, education='mca')
Mine=dict(name='vara', lastname='prasad', age=25,education='mca')
"""print(Me==Mine)
Me['age']=22
print(Me)

Me={"CS":[106,107,110],"MATH":[51,113]}
print(Me.get("CS"))
print(Me.get("MATH"))

del Me["name"]


Me.pop("age")
print(Me)

print(Mine.keys())
print(Mine.values())
print(Mine.items())
print(len(Mine.keys()))
for value in Mine.values():
    print(value)
print(Mine.copy())
t=("name","prasad")
print(t)"""
fish=(1,2,"red","blue")
print(fish[0])
print(len(fish))
t1=12345,54321,'abc'

x,y,z=t1
print(x)
print(y)
print(z)

a=10
b=20
a=a^b
b=a^b
a=a^b
print(a,b)
