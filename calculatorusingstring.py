#TRY ONE
#Calculator using string
input1=(input("Enter the number of first one "))
input2=(input("Enter the number of second input"))
str1=int(input1)
str2=int(input2)
print("*********Enter the operator to perform +,-,*,/,%**********")
operator=input("Enter the operator which one u want:")

if operator == '+':
    print(str1+str2)
elif operator =='-':
    print(str1-str2)
elif operator =="*":
    print(str1*str2)  
elif operator =='/':
    try:
        print(str1/str2)
    except:
        print("invalid input")
elif operator =='%':
    print(str1%str2)
else:
    print("invalid input")






