#Q1
sentance=input("write a sentence")
space=sentance.count(" ")
if space>0:
    print(space)
else:
    print(len(sentance))

#Q2
year=int(input("enter year-"))
if year%4==0:
    leap_year=True
else:
    leap_year=False
month=int(input("Month-"))
if month in (1,3,5,7,8,10,12):
    daysinmonth=31
elif month==2:
    if leap_year:
        daysinmonth=29
    else:
        daysinmonth=28
else:
    daysinmonth=30

day=int(input("Day-"))
if daysinmonth>day:
    day +=1
else:
    day=1
    if month==12:
        month=1
        year +=1
    else:
        month +=1
print("the next day is {}/{}/{}".format(day,month,year))

#Q3
list1=list(map(int,input("Enter the numbers separated by space:").split()))

list2=[]
for e in list1:
    t=(e,e*e)
    list2.append(t)

print("List containing (n,n^2) is shown below:")
print(list2)

#Q4
grade_point=int(input("Enter grade points:"))
dic={10:"Your grade is 'A+' and Outstanding performance.",
     9:"Your grade is 'A' and Excellent performance.",
     8:"Your grade is 'B+' and Very Good performance.",
     7:"Your grade is 'B' and Good performance.",
     6:"Your grade is 'C+' and Average performance.",
     5:"Your grade is 'C' and Below Average performance.",
     4:"Your grade is 'D' and Poor performance."}
     
if 4<=grade_point<=10:
        statement=dic.get(grade_point)
        print(statement)
else:
       print("Error Please enter grade in range [4,10]")

#Q5
input_str=("ABCDEFGHIJK")
i=0
while len(input_str)-i*2>=1:
    print(" "*i, input_str[0:len(input_str)-i*2])
    i=i+1

#Q6
repeat="Y"
dic={}
dic2={}

liste=["Y","y","n","N"]
while repeat=="Y" or repeat=="y":
    name = str(input("Enter student name:"))
    sid = int(input("Enter student SID:"))
    if sid<0:
        print("\nError\nSID can't be negative\n")
    else:      
        dic.update({sid: name})
        dic2.update({name:sid})
        repeat = str(input("Enter Y to continue or N to end:"))
    if repeat=="N" or repeat=="n":
        break
    elif (not (repeat in liste)):
        print("\nError\nPlease enter valid input['Y' or 'N']")
        repeat=str(input("\nEnter Y to continue or N to end:"))

print("Q.6(a)")
print("The Dictionary containing {'SID':'Name'} is shown below")
print(dic)

print("Q.6(b)")
list_k=sorted(dic2)
dic3={}
for ele in list_k:
    dic3.update({dic2.get(ele):ele})
print("The Dictionary after sorting according to name:")
print(dic3)

print("Q.6(c)")
sort_dic = sorted(dic)
dic4 = {}
for va in sort_dic:
    dic4.update({va: dic.get(va)})
print("The Dictionary after sorting according to SID:")
print(dic4)

input_sid=int(input("Enter Sid"))
name1=dic.get(input_sid)
print(name1)

#Q7
steps=int(input("enter the number of terms"))
a=0
b=1
i=0
list1=[]
while i<steps:
    c=a+b
    print(a)
    list1.append(a)
    b=a
    a=c
    i+=1
print("average of the series is:",sum(list1)/len(list1))

#Q8
set1= {1, 2, 3, 4, 5}
set2= {2, 4, 6, 8}
set3= {1, 5, 9, 13, 17}

print(f"Set1= {set1}\nSet2= {set2}\nSet3= {set3}")
print("\nQ.8(a)")
print("\nA new Set of all 'elements that are in Set1 and Set2 but not both' is:")
set_sym_dif=set1.symmetric_difference(set2)
print(set_sym_dif)

print("\nQ.8(b)")
print("\nA new set of all elements that are 'in only one of the three sets Set1,Set2 and Set3' is:")
set_u1=set1.union(set2)

set_uf=set_u1.union(set3)

set_i1=set1.intersection(set2)

set_if=set_i1.intersection(set3)

set_12=set1.intersection(set2)

set_23=set2.intersection(set3)

set_13=set1.intersection(set3)

set_f1=set_uf-set_12-set_23-set_13
print(set_f1)

print("\nQ.8(c)")
set_c1=set_12.union(set_23)

set_c2=set_c1.union(set_13)

set_final=set_c2-set_if

print("\nA new set of elements that are 'exactly in two of the sets Set1, Set2 and Set3' is:")
print(set_final)

print("\nQ.8(d)")
set_d={1,2}
set_d.clear()
for i in range(1,11):
    set_d.add(i)
set_new=set_d-set1

print("\nA new set of all Integers in the 'range 1 to 10' that are 'not in Set1' is:")
print(set_new)

print("\nQ.8(e)")
set_e=set_d-set_uf
print("\nA new set of all Integers in the range 1 to 10 that are not in Set1,Set2 and Set3.")
print(set_e)