#Write a python program to find an average of two numbers entered by the user.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

c = (a+b)/2 #always we shoud make bracket if we want to add first, it also use boadmas
# c = a/2+b/2 we can do by this type alse

print("Average of both number is: ",c)