class MathOperations:
    def add(self, num1, num2, num3=0):
        return num1+ num2+num3


mop = MathOperations()
print(mop.add(5, 3))       
print(mop.add(10, 7, 9))  
