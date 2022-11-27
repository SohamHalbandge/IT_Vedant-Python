l1 = [1,2,3,4,5,6,7]
print([i for i in l1])
print([i**2 for i in l1])
"""
Syntax :
variable = [output/expression for i item in list/range]

variable = [output/expression for item in range/list if condition]
"""
print([i for i in range(2,51,2)])
print([i for i in range(1,51,2)])
#For loop
l1 = ['red' , 'blue' , 'green' , 'black'] 
emp_l1 = []
for i in l1:
    first_letter = i[0] 
    emp_l1.append(first_letter)
print(emp_l1)
#List comprehension
print([i[0] for i in l1])
#
s1 = "i love python programming"
words = s1.split(" ")
print(words)
d = {}
for i in words:
    d[i.upper()] = len(i)
print(d)
#Using list comprehension
print([[i.upper(),len(i)] for i in words])
##
t = ((i for i in range(1,11)))
print(tuple(t))
##
d = {'a' : 1 , 'b' : 2}
item = {i for i in d.values()}
print(item)
##
d = {'a' : 1 , 'b' : 2}
item = {i for i in d.items()}
print(item)
print(type(item))
