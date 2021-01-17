list1 = [1, 2, 3]

list1.append(4)
print(list1)

print(list1.count(10))
print(list1.count(2))

x = [1, 2, 3]
x.append([4,5])
print(x)

x = [1,2,3]
x.extend([4,5])
print(x)

print(list1.index(2))

#print(list1.index(12))

print(list1)
print(len(list1))

list1.insert(2, 'inserted')
print(list1)
print(len(list1))

ele = list1.pop(1)
print(list1)
print(ele)

list1.remove('inserted')
print(list1)
print(len(list1))

list2 = [1,2,3,4,5]
list2.remove(3)
print(list2)

list2.reverse()
print(list2)

list2.sort()
print(list2)

list2.sort(reverse=True)
print(list2)


x = 'hello world'
y = x.upper()
print(y)

x = [1,2,3]
y = x.append(4)
print(y)

x = [1,2,3]
y = x.copy()
y.append(4)
print(x)
print(y)