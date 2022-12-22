#Q1

a=int(input("Value of a"))
b=int(input("Value of b"))
c=int(input("Value of c"))
d=(a+b+c)/3
print("Average of a,b,c is",d)

#Q2
gross_income=float(input("Enter gross income"))
dependents=int(input("Enter number of dependents"))
standard_ded=10000
dependent_ded=3000
tax_rate=0.2
taxable_income=gross_income-standard_ded-(dependent_ded*dependents)
tax=taxable_income*tax_rate
print("Tax=",tax)

#Q3
total_sec= int(input("enter seconds"))
minutes= total_sec//60
sec=total_sec%60
print("Minutes-", minutes, "seconds-", sec)

#Q4
a="25"
b=25
c=25.0
d=int(a)+b+int(c)
e=str(d)
print(e)

#Q5
import math
i=0
for i in range(0,345,15):
    a=math.sin(math.radians(i))
    b=math.cos(math.radians(i))
    print(round(a,4),round(b,4))