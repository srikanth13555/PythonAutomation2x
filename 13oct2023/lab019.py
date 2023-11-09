# Identity operator
# is returns True if both variable are the same object
# is not Returns True if both varaibale are not the same object

x = [1, 2, 3]
y= [1, 2, 3]



print(x is y)
print(id(x))
print(id(y))

print(x is y)
print(x is not y)