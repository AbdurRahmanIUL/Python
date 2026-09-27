# String is a data type in python.
# String is a sequence of characters enclosed in quotes

name = "Abdur Rahman"
print(name)

a = 'Ron' #we can use single quoted string
b = "Ron" #we can use double quoted string
c = '''Ron''' #we can use triple quoted string and instant of ' we can also use "

'''String Sclicing'''

#String is immutable in python , means can not be changed.
# A string in python can be sliced for getting a part of the strings.
#We use it in large bracket []

#name = "Abdur Rahman"  #it is above given so , I have commeted it.

#Positive slicing: starts from starting and index 0
nameshort = name[0:3] #start from index 0 all the way till 3 excluding 3
#nameshort = name[index_start:index_end] , how we do indexing
print(nameshort)
character1 = name[0]
print(character1)

