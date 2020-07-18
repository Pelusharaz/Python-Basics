#The following program is to show various uses of variables in python
#integer assignment
institution = "zetech University"
Name = "Pelu Jeremiah"
Hobbies ="Programming,Gaming"
#prints Results
print(institution)
print(Name)
print(Hobbies)
#Assigning a single value to multiple variables
a=b=c=d=25
#Prints results
print(a)
print(b)
print(c)
print(d)
#Assigning different values to multiple variables
a,b,c=20,30,56
#print results
print(a)
print(b)
print(c)

p="pelusharaz"
p="the best programmer"
#prints result
print(p)
#operators with variables
p="pelusharaz"
q=" loves programming"
a=" with python"
#results
print(p+q+a)



#global and local variables
def f():
    global s
    s="never"
    print(s)
s="How do i become a good programmer"
print(s)
 #global scope
s="pretend to be one"
print(s)
s="when do i stop"
print(s)
f()   
