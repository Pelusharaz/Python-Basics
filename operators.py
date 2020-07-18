#This is a program to show how different operators work
a=4
b=2
#examples of arithmetic operators
#addition of numbers
add=a+b
#subtraction of numbers
sub=a-b
#multiplication of numbers
mul=a*b
#division (float) of numbers
div=a/b
#division (floor)of numbers
div2=a//b
#modulo of numbers
mod=a%b

#print results
print(add)
print(sub)
print(mul)
print(div)
print(div2)
print(mod)

#examples of relaional operators
#a > b is True
print(a>b)
#a < b is False
print(a<b)
# a != b is true
print(a!=b)
#a == b is false
print(a==b)
#a >= b is True
print(a>=b)
#a <= b is false
print(a<=b)

#Examples of Logical operators
x=True
z=False
#print x or z is true
print(x or z)
#print X AND z is False
print(x and z)
#print not is True
print(not z)

#Bitwise operators
a=6
b=6
#Prints Bitwise AND operation
print(a & b)
#prints Bitwise Or operation
print(a | b)
#prints Bitwise Not operation
print( ~b)
#prints Bitwise XOR operation
print(a ^ b)
#Prints Right shift operation
print(a >> 2)
#prints left shift operation
print(a << 2)

#membership operators
z='pelu jeremiah'
q='loves coding'

#prints True
print('p' in z)

#prints true
print('loves' not in z)

#prints false
print('c'in z)