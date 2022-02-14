#question 1
print("SOLUTION TO QUESTION 1")
#string_entered=input("Enter the input: ")

print('Solution 1')
string=input('Enter the string: ')
upper_string=string.upper()
new_string=upper_string.split()

if len(new_string)==1:
    list_new=[]
    for i in upper_string:
        list_new.append(i)
    dict1={}
    for count in list_new:
        if count in dict1:
            dict1[count]=dict1[count]+1
        else:
            dict1[count]=1
    print(dict1, "\n")
else:
    dict2={}
    for word in new_string:
        if word in dict2:
            dict2[word]=dict2[word]+1
        else:
            dict2[word]=1
    print(dict2,"\n")



#question 2
print("SOLUTION TO QUESTION 2")

#Taking input from user
day_date=int(input('Please enter Day- '))
month_date=int(input('Please enter Month- '))
year_date=int(input('Please enter Year- '))


#Removing all the invalid cases
if day_date>30 and month_date in {2, 4, 6, 9, 11}:
    condition=False
elif day_date>31 and month_date in {1, 3, 5, 7, 8, 10, 12}:
    condition=False
elif (day_date == 29 or day_date == 30) and month_date==2 and year_date%4!=0:
    condition=False
elif day_date==30 and month_date==2 and year_date%4==0:
    condition=False
else:
    condition=True
if month_date>12:
    condition=False


#After checking the condition, following if-else statement is executed
if condition:
    #checking and changing for new year
    if day_date==31 and month_date==12:
        temp_year= year_date + 1
    else:
        temp_year=year_date
    if month_date==12 and day_date==31:
        temp_month=1
    else:
        temp_month=month_date

#changing dates
    #checking for months with 31 days
    if month_date in {1, 3, 5, 7, 8, 10, 12}:
        if day_date==31:
            next_day=1
            if month_date!=12:
                temp_month= month_date + 1
            else:
                temp_month=1
        else:
            next_day= day_date + 1
    #checking for the month of february
    elif month_date==2:
        if year_date%4==0:
            if day_date==29:
                next_day=1
                temp_month=3
            else:
                next_day= day_date + 1
        else:
            if day_date==28:
                next_day=1
                temp_month=3
            else:
                next_day= day_date + 1

    #covering all the remaining cases
    else:
        if day_date==30:
            next_day=1
            temp_month= month_date + 1
        else:
            next_day= day_date + 1
    #printing the calculations
    print(f"Next Date is: {next_day}/{temp_month}/{temp_year}","\n")

else:
    #gives a warning and ends the program
    print("That's not a valid date","\n")

#question 3
print("SOLUTION TO QUESTION 3","\n")
x=int(input("Enter a number 1 : "))
y=int(input("Enter a number 2 : "))
z=int(input("Enter a number 3 : "))

#tuples
t_1=(x,x*x)
t_2=(y,y*y)
t_3=(z,z*z)

#generating a list from the above tuples...
req_list=[t_1,t_2,t_3]
print("The required list of tuples with the second element as the square of the first element is: ", req_list,"\n")


#question 4
print("SOLUTION TO QUESTION 4","\n")
grade_point=int(input("Enter your grade point: "))
#from the information in given 
letter_grade={4:'D',
              5:'C',
              6:'C+',
              7:'B',
              8:'B+',
              9:'A',
              10:'A+'}
performance={4:'Poor',
             5:'Below Average',
             6:'Average',
             7:'Good',
             8:'Very Good',
             9:'Excellent',
             10:'Outstanding'}

if (grade_point>=4 or grade_point<=10):
    print("Your grade is", " ", letter_grade.get(grade_point) ," ", "and", " ", performance.get(grade_point),"\n")

else:
    print("ERROR")
    print("PLEASE CHECK THE VALUE ENTERED AND TRY AGAIN","\n")



#question 5
print("SOLUTION TO QUESTION 5","\n")

string='ABCDEFGHIGKJ'
j=0
for row in range(1,7):
    for column in range(0,row-1):
        print(' ',end='')
    
    s=string[0:11-j]
    print(s)
    j=j+2


#question 6
print("SOLUTION TO QUESTION 6","\n")

dictionary={}
while True:
     name=input("Enter the name: ")
     SID=int(input("Enter the SID: "))
     dictionary[SID] = name
     if input('''If you want to feed more details type "Y" else "N":''').upper() =='Y':
         continue
     else:
        print(f"Students details are as follows: (SID, Student name) \n{list(dictionary.items())}")
        print(f"\nSorted dictionary by student name:{sorted(dictionary.items(), key= lambda v:(v[1]))}")
        print(f'\nSorted dictionary by SID: {sorted(dictionary.items())}')
        search_SID=int(input("\nEnter the SID whose name you want to know:"))
        if search_SID in dictionary:
            print(f"The name of the student with SID {search_SID} is :{dictionary[search_SID]}\n")
        else:
            print("Enter the SID from the data you created.\n")
        break

#part a
for key,value in dictionary.items():
    print(f"{key} is {value}")

#part b
dictionary_sort_values= sorted(dictionary.values())
print(f"value sorted dictionary is {dictionary_sort_values}")


#part c
dictionary_sort_keys= sorted(dictionary.keys())
print(f"Keys sorted dictionary is {dictionary_sort_keys}")


#part d
SID_tbf=int(input("Please enter the student's SID whose detail you need- "))
if SID_tbf in dictionary.keys():
    print(f"Name of the required student is {dictionary[SID_tbf]}")
else:
    print("The SID is not present in the given Data","\n")


#question 7
print("SOLUTION TO QUESTION 7","\n")

number=int(input("Total elements of Fibonacci sequence that you want(must be greater than 1)- "))
a_n1=1
a_n2=0
n=0
#sum of the first two terms
sum=a_n1+a_n2

#printing the initial two terms 
print(a_n2)
print(a_n1)

#Printing the remaining fibonnaci terms
while n<number-2:
    a_n=a_n2+a_n1
    a_n2=a_n1
    a_n1=a_n
    print(a_n)
    n=n+1
    sum+=a_n
average=sum/number
#printing the program end prompt
print(f"Average of total {number} terms of sequence is:{average} ")

#question 8
print("SOLUTION TO QUESTION 8","\n")

s_1 = {1,2,3,4,5}
s_2 = {2,4,6,8}
s_3 = {1,5,9,13,17}

#part a
inter_s1_s2= s_1.intersection(s_2)
print("Set of all elements that are in Set1 and Set2 but not both:", inter_s1_s2)

#part b
only_elements=s_1^s_2^s_3
print(f"Set of elements that is only present in one set is: {only_elements}")

#Part C
only_in_two=(s_1|s_2|s_3)- (s_1^s_2^s_3)-(s_1&s_2&s_3)
print(f"Set of elements that is only present in two set is: {only_in_two}")


#part d
new_set1=set()
for n in range(1,11):
    new_set1.add(n)
not_common=new_set1- s_1
print(f"set of all integers in the range 1 to 10 that are not in Set1: {not_common}")


