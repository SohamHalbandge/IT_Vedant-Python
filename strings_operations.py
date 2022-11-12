s1 = "I love Python Programming"
print(s1)
s2 = "python programming"
print(s2)
#length of string
print(len(s1))
print(len(s2))
#type of data
print(type(s1))
print(type(s2))
#Indexing
print(s2[0])
print(s2[5])
print(s2[17])
print(s2[-1])
print(s2[-18])
#slicing
print(s2[0:5])
print(s2[0:6])
print(s2[7:17])
print(s2[7:])
print(s2[0::2])
print(s2[0::])
print(s2[1::2])
print(s2[-1::-1])
print(s2[::-1])
print(s2[-18:-12])
#slicing of s1
print(s1[7:13])
#concatenation
s3 = "python"
s4 = "programming"
print(s3+s4)
print('I love'+'python')
print(s3 + " " + s4)
print((s3 + " " )* 3)
#Removing Spaces
s5 = "     Python Programming     "
print(s5)
print(s5.strip())
print(s5.lstrip())
print(s5.rstrip())
#Finding substring in a string
s1 = "Learning Python is very easy"
print(s1.find("Python"))
print(s1.find("Java"))
print(s1.find('e'))
print(s1.find("is",15,))
print(s1.find("is",15,15))
print(s1.index("Python"))
#print(s1.index("Java")) ---> This will throw an error
#COunting a string
s1 = 'abababababababababbabababa'
print(s1.count('a'))
print(s1.count('d'))
print(s1.count('ab'))
#String is immutable
s1 = 'Python'
#s1[0] = 'A'
print(s1)
#Replacing a string and storing in a new variable
s2 = "learning python is difficult"
s = s2.replace('difficult' , 'easy')
print("old string:",s2)
print("new string:",s)
#Splitting a  string
s1 = 'Learning python is easy'
list_of_words = s1.split(" ")
print(list_of_words)
print(type(list_of_words))
#Splitting email id
s1 = "abc@gmail.com"
print(s1.split('@'))
#Joining a string
l1 = ['i' , 'love' , 'python' , 'programming']
s = "-".join(l1)
s1= " ".join(l1)
print(s)
print(s1)
#Changes case of a string
#Upper  case
print(s1.upper())
#Lower Case
print(s1.lower())
#Swap Case
print(s1.swapcase())
#Title
print(s1.title())
#Capitalise
print(s1.capitalize())

#To check the type of data in string
s1 = 'abc123'
s2 = 'python'
s3 = '123'
s4 = "PYTHON"
print(s1.isalnum())
print(s2.isalnum())
print(s3.isalnum())
print(s1.isalpha())
print(s2.isalpha())
print(s3.isalpha())
print(s1.isdigit())
print(s2.isdigit())
print(s3.isdigit())
#TO check the cases in the strings
print(s2.islower())
print(s4.isupper())
print(s3.isupper())

#Formatting a string
name = "Akash"
age = 25
salary = 25000
print("Name:",name,"Age:",age,"Salary:",salary)
print("Name:",name)
print("Age:",age)
print("Salary:",salary)
print("My Name is {} , My age is {} , My Salary is {}".format(name,age,salary))
print("My Name is {0} , My age is {1} , My Salary is {2}".format(name,age,salary))
print("My Name is {2} , My age is {1} , My Salary is {0}".format(name,age,salary))

#fstring
print(f"Hello {name}")
print(f"Age is {age}")
print(f"Salary is {salary}")
print(f"Hello {'Name'} : {name}")

#Escape Sequence
print("python\nprogramming")
print("python\\nprogramming")
print("Learning \"Python\" is very fun") 
