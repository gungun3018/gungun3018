print("ASSIGNMENT 4")


#QUESTION 1
print("SOLUTION TO QUESTION 1")

#using recursion...
n=int(input("Enter the number: "))
def Tower_Of_Hanoi(n , source, destination, auxiliary):
    if n==1:
        print ("Move disk 1 from source",source,"to destination",destination)
        return
    Tower_Of_Hanoi(n-1, source, auxiliary, destination)
    print ("Move disk",n,"from source",source,"to destination",destination)
    Tower_Of_Hanoi(n-1, auxiliary, destination, source)

print(Tower_Of_Hanoi(n,'A','B','C'),"\n")
# A,B,C are the name of rods


#QUESTION 2
print("SOLUTION TO QUESTION 2 ","\n")
#method 1
n=int(input("Enter the number of the rows: "))

# Print Pascal's Triangle in Python
from math import factorial
 
for i in range(n):
    for j in range(n-i+1):
 
        # for left spacing
        print(end=" ")
 
    for j in range(i+1):
# nCr = n!/((n-r)!*r!)
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")

    # for new line
    print()

    
#method 2

n = int(input("Enter the number of rows:"))  
  
# iterarte upto n  
for i in range(n):  
   # adjust space  
   print(' '*(n-i), end='')  
  
   # compute power of 11  
   print(' '.join(map(str, str(11**i))))  


#QUESTION 3
print("SOLUTION TO QUESTION 3 ","\n")
print("The number should be an integer.")
n_1=int(input("Enter the first number: "))
n_2=int(input("Enter the second number: "))

if n_1!=0 :
    #PART A 
    print("Function is callable.")
    quo, rem=divmod(n_1, n_2)
    print(f"Quotient obtained={quo}\nReminder obtained={rem:2f}")
    
    #PART B
    if quo==0:
        print("Quotient is zero.")
    else:
        print("Quotient is non-zero.")
    if rem==0:
        print("Remainder is zero")
    elif (quo,rem)==0:
        print("Both the values are zero.")
    else:
        print("Values are non-zero.")
        
    #PART c
    list_01=(quo, rem)+(4, 5, 6)
    print(list_01)
    list_02=[]
    for i in list_01:
        if i>4 :
            list_02.append(i)
    print("\nThe values which are greater than 4 are:", list_02)
    
    #PART d
    print("\nConversion to set datatype:", set(list_02))
    
    #PART E
    st=frozenset(list_02)
    print("\nMaking  the set immutable:", st)
    
    #PART F
    print("\nThe maximum value from set is:", max(st))
    print("The hash value for the maximum value:", hash(max(st)))
else:
    print("Function is not callable")


#QUESTION 4
print("SOLUTION TO QUESTION 4 ","\n")
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        print("Instructor is called.", "\n")

    def __del__(self):
        print("Object gets deleted as destruction is called.","\n")

s_1=Student("Gungun", 23)
del s_1

#QUESTION 5
print("SOLUTION TO QUESTION 5 ")
print()

#creating the class 
class income :      
     def __init__ (self,name,salary) :
         self.name=name 
         self.salary=salary  
     def __del__ (self) :
         print('Record of ',self.name,'destroyed')
     def show(self):
        print(f"{self.name}\t{self.salary}")
         
# creating the objects 
empolyee_1=income('Mehak',40000)    
empolyee_2=income('Ashok',50000)
empolyee_3=income('Viren',60000)

# printing the details
print("Name\tSalary")
empolyee_1.show()
empolyee_2.show()
empolyee_3.show()

empolyee_1.salary=70000
 
# updating the salary 
print('\nUpdated salary of',empolyee_1.name,'is',empolyee_1.salary)

print ('\nPart b')
del empolyee_3
print("The record of Viren has been deleted.")
# deleting the record of Viren 
print()



#QUESTION 6
print("SOLUTION TO QUESTION 6 ")

# Defining the function 
def test(s):  
    if s=='' :
         return [s]
    else :
         word=[]
         for i in test(s[1:]) :
             for k in range(len(i)+1) :
                 word.append(i[:k]+s[0]+i[k:])
         return word
        
# Taking input from the users 
w_1=input("George, Enter a word to test your friendship: ")
w_2=input("Barbie, Give a meaningful word containing same letter of the word given by your friend: ")

# checking

if w_2 in test(w_1) :    
    print("TRUE FRIENDSHIP")
else:
    print("The word entered by Barbie is not meaningful. Hence, FAKE FRIENDSHIP")
