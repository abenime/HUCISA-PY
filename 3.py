num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
op=input("Enter the operand (*,/,+,-): ")

result=0

if op=="*":
    result=num1*num2
elif op=="/":
    result=num1/num2
elif op=="+":
    result=num1+num2
elif op=="-":
    result=num1-num2
else:
    print("Incorrect Operand")
    
print(f'Result = {result}')