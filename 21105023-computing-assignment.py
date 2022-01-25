# question 1
print("SOLUTION TO QUESTION: 1")
s1 ="Python is a case sensitive language."

# a) length of the string..
print("The length of the string is: ",len(s1),"\n")

# b)reversing the order of the string...
print("The reversed order of the string is: ",s1[::-1],"\n")

# c)slicing a string
new_s1=s1[10:26]
print("The sliced string is: ", new_s1,"\n")


# d)replacing 
print("The replaced string is:",s1.replace("a case sensitive ","object orientated "),"\n")

# e)finding index
print("The index of substring 'a' is: ", s1.find("a"),"\n")

#f)removing white spaces
print("The required string is: ",s1.replace(" ",""),"\n")


#question 2
print("SOLUTION TO QUESTION: 2")
Name= "Gungun"
SID="21105023"
Department_name="ECE"
CGPA="9.9"
print("Hey," + Name + " " + "here")
print("My SID is " + " " + SID)
print("I am from " + " " + Department_name + " " + "department" + " " + "and my CGPA is" + " " + CGPA,"\n")


#question 3
print("SOLUTION TO QUESTION: 3")
a=56
b=10
#a)
print("a&b: ",a&b)
#b)
print("a|b: ",a|b)
#c)
print("a^b: ",a^b)
#d)
print("a<<2 ",a<<2)
print("b<<2 ",b<<2)
#e)
print("a>>2",a>>2)
print("b>>2",b>>2,"\n")

#question 4
#findig the greatest of the three numbers...
print("SOLUTION TO QUESTION: 4")
num_1=int(input("Enter your number 1:"))
num_2=int(input("Enter your number 2:"))
num_3=int(input("Enter your number 3:"))

if (num_1>num_2 and num_1>num_3):
    print("num_1 is the greatest","\n")
    
elif(num_2>num_3 and num_2>num_num_1):
    print("num_2 is the greatest","\n")
    
else:
    print("num_3 is the greatest.","\n")


#question 5
print("SOLUTION TO QUESTION: 5")
string=input("Enter you message here: ")

if ("name" in string):
    print("YES","\n")
else:
    print("NO","\n")

#question 6
print("SOLUTION TO QUESTION: 6")
#the three sides of triangle respectively are:
side_1=int(input("Enter the length of first side: "))
side_2=int(input("Enter the length of second side: "))
side_3=int(input("Enter the length of third side: "))

if(side_1+side_2>side_3):
    print("YES, They form a triangle.")

elif(side_3+side_2>side_1):
     print("YES, They form a triangle.")

elif(side_1+side_3>side_2):
    print("YES, They form a triangle.")
    
else:
    print("NO")
    