#Q1.a

a="Python is a case sensitive language."
print(len(a))

#q1.b
reverse_a=a[::-1]
print(reverse_a)

#q1.c
b=a[10:26]
print(b)

#q1.d
replaced_a=a.replace("a case sensitive","object oriented")
print(replaced_a)

#q1.e
find_a=a.find('a')
print(find_a)

#q1.f
space_removed=a.replace(" ","")
print(space_removed)

#Q2
name=input("Enter Name")
sid=input("Enter SID")
department=input("Enter Department")
cgpa=float(input("Enter CGPA"))
print("Hey,", name.capitalize(),"Here!" )
print("\n My SID is", sid)
print("\n I am from", department.capitalize(),"department and my CGPA is", cgpa)

#Q3
a=56
b=10
c=a&b
print("Value of a&b=",c)
d=a|b
print("Value of a|b=",d)
e=a^b
print("Value of a^b=",e)
f=a<<2
g=b<<2
h=a>>4
i=a>>4
print("Left shift both a and b with 2 bits",f,g)
print("Right shift a with 2 bits and b with 4 bits",h,i)

#Q4
a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=int(input("Enter third number"))
if a>=b and a>=c:
    print("Largest number is", a)
elif b>=a and b>=c:
    print("Largest number is", b)
elif c>=a and c>=b:
    print("Largest number is", c)
else:
    print("error")

#Q5
input_string=str(input("input"))
if "name" in input_string:
    print("true")
else:
    print("false")

#Q6
a=int(input("Length of first side"))
b=int(input("Length of second side"))
c=int(input("Length of third side"))
if a<b+c and b<a+c and c<a+b:
    print("true")
else:
    print("false")