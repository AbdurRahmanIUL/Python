#Negative slicing: starts from ending and with index -1

name = "Abdur Rahman" #print(len(name)): output:12 it also count space index 1.

print(name[0:3]) #it is positive slicing example

print(name[-4:-1]) #output = hma, remember its not showing last n
print(name[8:11]) #Tip:we should change negative index to positive index for simple.

print(name[:4])

#below two lines are equal
print(name[1:])    # is same as print(name[1:11])
print(name[1:11])  # is same as print(name[1:])

# Slicing with Skip Value
# We can provide a skip value as a part of our slice like this:

word = "amazing"
print(word[1:6:2]) # mzn

# Other advanced slicing techniques:
word = "amazing"
print(word[-7:-1]) # amazin
print(word[:7]) # amazing
print(word[0:]) # amazing
