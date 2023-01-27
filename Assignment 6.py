a=int(input("Enter a number "))
def perfectnumber(a): 
    i=1
    sum=0
    while i<a:
        if a%i==0:
            sum=sum+i
            i+=1
        else:
            i+=1
    if sum==a:
        return "Number %d is a perfect number"%(a)
    else:
        return "Number %d is a not perfect number"%(a)

print(perfectnumber(a))

#Q2
a=input("Enter Sentence: ")
def palindrome(a):
    a=str(a)
    a=a.replace(' ','')
    b=a[::-1]
    if a==b:
        print("Yes it is a palindrome")
    else:
        print("No it is not a palindrome")

palindrome(a)

#Q3
n=int(input("enter number of rows "))
r=0
def fact(n):
    if n==1:
        return 1
    elif n==0:
        return 1
    else:
        return n*fact(n-1)
def comb(n,r):
    return fact(n)//(fact(r)*fact(n-r))

i=0
space=n
print(" "*space,end="")
while i<n:
    j=0
    while j<=i:
        a=str(comb(i,j))
        x=1
        while x in range(len(a)):
            a=a[x]
            x+=1
        print(a,end=" ")
        j+=1
    space-=1
    print()
    print(" "*space,end="")
    i+=1

#Q4

a=input("Enter Sentence: ")
def panagram(a):
    a=str(a)
    a=a.replace(' ','')
    set1=set()
    i=0
    while i<len(a):    
        set1.add(ord(a[i]))
        i+=1
    set2=set()
    x=91
    while x<123:
        set2.add(x)
        x+=1
    if set1.issubset(set2):
        print("true")
    else:
        print("false")
panagram(a)

#Q5
a=input("Enter hyphen-separated sequence of words ").split("-")
a=sorted(a)
print("-".join(a))

#Q6
def student_data(student_name , student_branch, student_id):
    print("Student name: ",student_name)
    print("Student branch: ",student_branch)
    print("Student ID: ",student_id)

student_data("Yatharth","Electrical",22104011)

#Q7
class Student:
    pass 
class Marks:
    pass 
student1 = Student()
marks1 = Marks()
print(isinstance(student1, Student))
print(isinstance(marks1, Student))
print(isinstance(marks1, Marks)) 
print(isinstance(student1, Marks))
print("Check whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object))
print(issubclass(Marks, object))
print()

#Q8
list=[]
def findTriplets(arr, n):
  
    found = False
    for i in range(0, n-2):
      
        for j in range(i+1, n-1):
          
            for k in range(j+1, n):
              
                if (arr[i] + arr[j] + arr[k] == 0):
                    list.append([arr[i],arr[j],arr[k]])
                    print(list)
                    found = True
      
    if (found == False):
        print(" not exist ")
  
arr = [-25, -10, -7, -3, 2, 4, 8, 10]
n = len(arr)
findTriplets(arr, n)

#Q9
class parantheses:
    def find(str):
        a= ['()', '{}', '[]'] 
        while any(i in str for i in a):
            for j in a:
                str = str.replace(j, '') 
        return not str 

s = input("Enter the sequence of parantheses : ")
if parantheses.find(s):
    print(s,"-","is balanced")
else:
    print(s,"-","is unbalanced")
