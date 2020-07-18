#in this programme i'll be running afew loops
#if statement
p=20
if(p>15):
 print ("20 is grater than 15")
print("syntax error")

#if else statement
q=4
if(q>0):
    print("true")
    print("q=is greater")
else:
    print("4 is lesser than 0")
    print("true")
print("both situations are false")

#nested if
p=20
if(p == 20):
    if(p<100):
        print("p is obviously smaller than 100")
        #this will be executed if the above is true
    if(p<50):
        print("p is smaller than 50 too")
    else:
        print("p is greater than 100 lol")

#if-elif-ladder
#i'll use a grading system to illustrate this
#grading system
grade=int(input('enter your mark: \n'))
if grade<100 and grade>=80:
    print ('grade is A')
elif grade>=60 and grade<=79:
    print('grade is B') 
elif grade>=40 and grade<=59:
    print ('grade is c')
elif grade>=30 and grade<=39:
    print ('grade is D')
else:
    print('fail')      

#now to the loops in python
# while loop
count=5
while(count <10):
    count= count+1  
    print("hello sharaz")        