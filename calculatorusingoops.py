class Calculator:
    
    def add(self,a,b):
        print(float(a)+float(b))
    def sub(self,a,b):
        print(float(a)-float(b))
    def mul(self,a,b):
        print(float(a)*float(b))
    def div(self,a,b):
        print(float(a)/float(b))
    def mod(self,a,b):
        print(float(a)/float(b)) 

user_input=input("Enter the input")#10+2
operands=user_input.split()
print(operands)

for i in operands:
    print(i)
    a=operands[0]
    b=operands[2]
    operator=operands[1]
obj1=Calculator()
#print("Give which operator you want to do (+,-,*,/,%)")
#operator=input("Enter the opoerator to perform ")

if operator=='+':
    print( obj1.add(a,b))
elif operator=='-':
    print( obj1.sub(a,b))
elif operator=='*':
    print( obj1.mul(a,b))
elif operator=='/':
    print( obj1.div(a,b))
elif operator =='%':
    print( obj1.mod(a,b))
else:
    print("invalid input")





