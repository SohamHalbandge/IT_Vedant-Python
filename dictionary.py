# %%
"""
Dictionary :-
- Key:Value pair
- Keys are Immutable
- Values are mutable
- Unordered --> Indexing and Slicing not allowed
- Duplicate keys are not allowed
- Duplicate values are allowed
- Dictionaries are mutable
- Created by using curly bracket and created with the help of {} or with the help of dict
"""
# %%
# Empty dictionary
d1 = {}
print(d1)
print(type(d1))
# %%
d1 = {"Name" : "Akash" , "Roll_No" : 12 , "marks" : 67 , "address" : "Thane"}
print(d1)
print(type(d1))
# %%
d1['Name']
# %%
d1['marks']
# %%
d1['address']
# %%
#Add key-value pair
d1['qualification'] = "B.E"
# %%
print(d1)
# %%
d1['department'] = 'Computer Science'
# %%
print(d1)
# %%
e1 = {'Name' : 'Pratik'}
e1.update({'Salary' : 5000 , 'Dept' : 'Accounts'})
print(e1)
# %%
print(d1.get('Name' , 'Name is not available'))
print(d1.get('Age' , 'Age is not available'))
# %%
#How to update the existing values in the dictionary
print(e1)
print(e1['Salary'])
# %%
e1['salary'] = (5000 + (5000*20)/100)
print(e1)
# %%
e1['Name'] = 'Pooja'
print(e1)
# %%
data = {'Teams' : ['MI' ,'CSK','RCB','KKR','RR','GL'] , "Wins" : [10,5,4,2,1,4]}
print(data)
# %%
print(data['Wins'])
# %%
print(data['Wins'][0])
# %%
print(data['Wins'][-1])
# %%
#Deletion
print(d1)
# %%
d1.pop('department')
# %%
print(d1)
# %%
d1.pop('Name')
print(d1)
# %%
d1.popitem()
# %%
print(d1)
# %%
d1.clear()
print(d1)
# %%
#built in functions
print(e1)
print(e1.keys())
print(e1.values())
print(e1.items())
# %%
#copy (Shallow copy)
e2 = e1.copy()
print(e2)
e3 = e1 #Deep copy
print(e3)
# %%
