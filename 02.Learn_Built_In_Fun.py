# List (mutable)
numbers = [2,3,5,9,13,18]

alfa = ['A','a','R','B','b','C','c','X','x','Y','z']
print(alfa)

# max() & min()
print(max(numbers))

#length of list
print(len(alfa))

#slicing on list
print(alfa[::-1],'\n')

#Append in list(to add any value at last position of the list)
numbers.append(0)
alfa.append('R')

print(numbers,'\n',alfa)

# insert()
numbers.insert(3,77)
print(numbers)

# index()
print('\n',alfa.index('B'))

# Extend():to extend list 
# we can't use like: numbers.extend(22,23,24,25) bcz it takes only one value in paranthesis () so we can provide it in square bracket []
numbers.extend([22,23,24,25])
print(numbers)

# To sort list
alfa.sort()
print(alfa)
# to reverse list
alfa.reverse()
print(alfa)

#slicing 
print(numbers[::2])
# Reverse slicing
print(numbers[::-1])

#sorting(list is mutable so after sorting List value changes)
numbers.sort()
print(numbers)

#tuple (immutable)
tp = (1,4,7,8)
# tuple is not callable so don't do : print(tp(2))
print(tp)
#slicing on tuple
print(tp[:2:])
print(tp[::-2])
