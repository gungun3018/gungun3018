# QUESTION 1:


#finding average of three numbers.....

print("ANSWER-1", "\n")
Number1=int(input(" Enter the 1st number:"))
Number2=int(input(" Enter the 2nd number:"))
Number3=int(input(" Enter the 3rd number:"))

#finding the average using the formula

Average = Number1 + Number2 + Number3 / 3

print("The average of the 3 numbers is",Average, "\n")



#Question 2

#calculating income tax following the required conditions...
 
print("ANSWER-2")
Gross_income=int(input("Enter the gross income to the nearest penny:"))
Dependents=int(input("Enter the number of dependents:"))

flat_tax_rate= 0.2
Standard_deduction= 10000
Dependent_deduction= 3000

Taxable_income= (Gross_income - Standard_deduction -( Dependent_deduction * Dependents))
tax=Taxable_income*flat_tax_rate
print("TAX comes out to be:",tax,'\n')



#QUESTION 3:

# general information about the student...

print("ANSWER-3","\n")

SID=int(input("SID:"))
Name=str(input("Name:"))
Gender=str(input("Gender: 'F','M','U' for female, male and unknown respectively"))
CGPA=float(input("CGPA:"))
Course=str(input("Course Name:"))
"
print(" STUDENT GENERAL INFORMATION...")




#QUESTION 4:


#displaying the marks of 5 students...

print("ANSWER-4", "\n")
A=int(input("Enter the marks of Student 1:"))
B=int(input("Enter the marks of Student 2:"))
C=int(input("Enter the marks of Student 3:"))
D=int(input("Enter the marks of Student 4:"))
E=int(input("Enter the marks of Student 5:"))
Marks=[A,B,C,D,E]
print("The marks of the 5 students are as follows:",Marks)
Marks.sort()
print("Sorted marks of 5 student:",Marks,"\n")


#QUESTION 5:


#list of colours....

print("ANSWER-5", "\n")
color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print('The list of colours is:',color,'\n')
#python program to remove the 4th element of the list...
color.pop(4)

print('The modified list of colours is:',color,'\n')

#second part of the question..
#replacing black aand pink with purple....
color[4:5]=['Purple']
print("The required list is:",color,'\n')



