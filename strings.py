'''creating strings'''
#using single quotes
string1='call me sharaz'
print("welcome to python strings:")
print(string1)

#using double quotes
string2="you are in the right hands"
print("\nlike coding?:")
print(string2)

#using tripple quotes
string3='''you
            sleep
            I
            code'''
print("\nmultiple strings:")
print(string3)            

#accessing characters in python
#to access the first character of string2
print(string2[0])

print("\nthe last character of string 3 is:")
print(string3[-1])

#string slicing
#i'll use string 1
print("\nslice characters"+"between the 6th and last")
print(string1[7:])

#updating strings
string4="you are in the right hands"
print("\ninitial string;")
print("\nlike coding?")
print(string4)

#updated string
string4="welcome on board"
print("\nupdated;")
print(string4)
#deleting strings

#escape sequencing
string5='''I'd code with python'''
print("using tripple quotes:")
print(string5)
string5='I\'d code with python'
print("\nusing single quotes:")
print(string5)

string5="i'd code with \"python\""
print("\nusing double quotes:")
print(string5)

#printing paths with the use of escape sequences
string5="C:\\OOP Python\\strings"
print("\nusing backslashes:")
print(string5)

#ignoring escape sequences
string6="mathematical calculation \x45\x52"
print("\nusing escape sequence:")
print(string6)

string6=r"mathematical calculation \*45\*52"
print("\nprinting the raw sring:")
print(string6)

#formatting of strings
string1="{} {} {}".format('call','me','sharaz')
print("\ndefault order:")
print(string1)

string1="{2} {1} {0}".format('my name','is','sharaz')
print("\npositional formatting:")
print(string1)

string1="{r} {s} {p}".format(r='call',s='me',p='sharaz')
print("\nkeyword formatting:")
print(string1)

#formatting integers
string1="{0:b}".format(20)
print("\nThe binary representation of 20 is:")
print(string1)

#formatting of floats
string1="{0:e}".format(20.2)
print("\nThe exponent representation of 20.2 is:")
print(string1)

#rounding off of integers
string1="{0:.2f}".format(1/20)
print("\none out of 20 is:")
print(string1)



