 #use of 'is' identity operator
x = 8
if (type(x) is int):
    print("true")
else:
    print("false")

x = 7.9
if (type(x) is not float):
    print("true")
else:
    print("false")
 
x = 40
y = 40
if (x is y):
    print("x & y SAME identity")

y = 40
if (x is not y):
    print("x & y have DIFFERENT identity")