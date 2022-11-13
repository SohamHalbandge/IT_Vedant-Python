# %%
"""
Set :
1. Unordered 
2. Duplicates are not allowed
3. Collection of hetrogeneous elements
4. Mutable
"""
# %%
#Sets are created by using {} separated by ,
# %%
s1 = {}
print(s1)
print(type(s1))
#Empty curly brackets gives us a dictionary
# %%
s2 = set()
print(s2)
print(type(s2))
# %%
s3 = {12,3,4,5,6,7,8.6,'python'}
print(s3)
print(type(s3))
# %%
#It gives error since it is unordered
#3[0]
# %%
s4 = set(range(10,61,10))
print(s4)
print(type(s4))
# %%
#Mutable
s5 = {"cat",'apple','banana',100,45,67,8.9,2.6}
print(s5)
# %%
#Add(x) : To add single element
s5.add('python')
print(s5)
# %%
s5.add("Java")
print(s5)
# %%
#2. Update(x,y,z) : Add multiple elements into the set
s1 = (10,20,30)
s5.update(s1)
print(s5)
# %%
l1 = [1,2,3,4,5]
s = {10 , 20 ,30}
s.update(l1)
print(s)
# %%
s1 = {1,1,1,1,2,2,2,3,3,3,3,4,4,4}
print(s1)
# %%
#Removing Duplicates of list by converting list to set
l1 = [1,1,1,1,2,2,2,2,3,3,3,4,4,4,5]
s1 = set(l1)
l1 = list(s1)
print(l1)
print(type(l1))
# %%
s1 = set(range(10,51,5))
print(s1)

# %%
#deletion
s1.pop()
# %%
s1.remove(40)
# %%
print(s1)
# %%
s1.discard(45)
print(s1)
# %%
#Remove element will give a error if element is not there
#Discard will not give a error
s1.discard(1999)
print(s1)
# %%
s1.clear()
print(s1)
# %%
del s1

# %%
#Mathematical Operation
#1. Union of the set
s1 = {10,20,30,40}
s2 = {30,40,50,60}
print(s1.union(s2))
print(s1)
print(s1|s2)
# %%
#2. Intersection
print(s1.intersection(s2))
print(s1&s2)
# %%
#Difference
s1 = {10,20 , 30, 40}
s2 = {30 , 40 ,50 , 60}
print(s2.difference(s1))

# %%
#Symmetric difference
#gives the elements from both the sides except the common elements
s1 = {10,20 , 30, 40}
s2 = {30 , 40 ,50 , 60}
print(s2.symmetric_difference(s1))
# %%

s1 = (10,20,30,40)
print(s1)
print(type(s1))
# %%
#TO make sets mutable to immutable
s2 = frozenset(s1)
# %%
print(s2)
# %%
print(type(s2))
# %%
