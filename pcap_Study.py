
def line_break():
    for x in range(0,25):
        print("*", end="")
    print("\n")


i = 250
while len(str(i)) > 72:
    i *= 2
else:
    i //= 2
print(i)


line_break()

n = 0
while n < 4:
    n += 1
    print(n, end = " ")
print("\n")

line_break()

x = 0
y = 2
z = len("Python")
x = y > z
print(x)

line_break()

Val = 1
Val2 = 0
Val = Val ^ Val2
Val2 = Val ^ Val2
Val = Val ^ Val2
print(Val)

line_break()

z, y, x = 2, 1, 0
x, z = z, y
y = y - z
#x, y, z = y, z, x
#z, y, x = x, z, y
y, z, x = x, y, z
print(x, y, z)
line_break()

a = 0
b = a ** 0
print(b)
if b < a + 1:
    c = 1
elif b == 1:
    c = 2
else:
    c = 3
print(a+b+c)

line_break()

i = 10
while i > 0:
    i -= 3
    print("*")
    if i <= 3:
        break
else:
    print("*")

line_break()

print("Example 1")
for i in range(1, 4, 2):
    print("*")
print("\n")
print("Example 2")
for i in range(1, 4, 2):
    print("*", end="")
print("\n")
print("Example 3")
for i in range(1, 4, 2):
    print("*", end="**")
print("\n")
print("Example 4")
for i in range(1, 4, 2):
    print("*", end="**")
print("***")
print("\n")

line_break()

x = "20"
y = "30"
print(x>y)
print(y>x)

line_break()

s = "Hello, Python!"
print(s[-14:15])

line_break()

lst = ["A", "B", "C", 2, 4]
del lst[0:-2]
print(lst)

line_break()

dict = {'a': 1, 'b': 2, 'c': 3}
for item in dict:
    print(item)

line_break()

s = 'python'
for i in range(len(s)):
    i = s[i].upper()
print(s, end="")
print("\n")

line_break()

#lst = [i//i for i in range(0, 4)]
sum = 0
for n in lst:
    sum += n
print(sum)

line_break()

lst = [[c for c in range(r)] for r in range(3)]
print(lst)
for x in lst:
    for y in x:
        if y < 2:
            print('*', end = "")
print("\n")

line_break()

lst = [2 ** x for x in range(0, 11)]
print(lst[-1])

line_break()

lst1 = "12,34"
lst2 = lst1.split(",")
print(len(lst1) < len(lst2))

line_break()

def fun(a, b = 0, c = 5, d = 1):
    return a ** b ** c

print(fun(b=2, a=2, c=3))

line_break()

x = 5
#f = lamdba x: 1 + 2
#print(f(x))

line_break()

from math import pi as xyz
#print(pi)
print(xyz)

line_break()

from random import randint
for i in range(10):
    #print(random(1,5))
    print(randint(1,5))

line_break()

x = 1 # line 1
def a(x):  # line 2
    return 2 * x  # line 3

x = 2 + a(x)  # LINE 4
print(a(x)) # line 5

line_break()


a = 'hello'
def x(a, b):
    z = a[0]
    return z
#print(x(a))

line_break()

s = 'SPAM'
def f(x):
    return s + 'MAPS'
print(f(s))

line_break()


def gen():
    lst = range(5)
    for i in lst:
        yield i*i

for i in gen():
    print(i, end="")
print("\n")

line_break()

print("Example 1")
x = 1
y = 0
#z = x%y
#print(z)
print("Example 2")
x = 1
y = 0
#z = x/y
#print(z)
print("\n")

line_break()

x = 0
try:
    print(x)
    print(1/x)
except ZeroDivisionError:
    print("ERROR MESSAGE")
finally:
    print(x+1)
print(x+2)

line_break()

class A:
    def a(self):
        print("A",end="")

class B(A):
    def a(self):
        print("B", end="")

class C(B):
    def b(self):
        print("B", end="")

a = A()
b = B()
c = C()

a.a()
b.a()
c.b()
print("\n")

line_break()

try:
    print("Hello")
    raise Exception
    print(1/0)
except Exception as e:
    print(e)

line_break()

#print("Example 1")
#class CriticalError(Exception):
#    def __init__(self, message='ERROR MESSAGE A'):
#        Exception.__init__(self,message)

#raise CriticalError
#raise CriticalError("ERROR MESSAGE B")

#print("Example 2")
#raise CriticalError("ERROR MESSAGE B")

line_break()


