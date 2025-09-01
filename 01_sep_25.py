class SampleCalculator():
    
    def Addition(self,num1,num2):
        print(f'{num1} + {num2} = {num1 + num2}')

    def Subtraction(self,num1,num2):
        print(f'{num1} - {num2} = {num1 - num2}')

    def Multiplication(self,num1,num2):
        print(f'{num1} * {num2} = {num1 * num2}')

    def Division(self,num1,num2):
        if num2 == 0:
            print('Division by Zero is not possible')
        else:
            print(f'{num1} / {num2} = {num1 / num2}')

    def FloorDivison(self,num1,num2):
        if num2 == 0:
            print('Division by Zero is not possible')
        else:
            print(f'{num1} // {num2} = {num1 // num2}')

    def ModularDivison(self,num1,num2):
        if num2 == 0:
            print('Division by Zero is not possible')
        else:
            print(f'{num1} % {num2} = {num1 % num2}')

    def Exponent(self,num1,num2):
        print(f'{num1} ** {num2} = {num1 ** num2}')

    def product_details(self):
        print(f'{self.obj} details:{self.model_num},{self.made_in},{self.color},{self.discount}')



obj1 = SampleCalculator()
obj2 = SampleCalculator()

print("All Arithmatic operations on obj1")
obj1.Addition(5,2)
obj1.Subtraction(5,2)
obj1.Multiplication(5,2)
obj1.Division(5,2)
obj1.FloorDivison(5,2)
obj1.ModularDivison(5,2)
obj1.Exponent(5,2)

print("All Arithmatic opeartions on obj2")
obj2.Addition(10,20)
obj2.Subtraction(44,4)
obj2.Multiplication(50,3)
obj2.Division(102,0)
obj2.FloorDivison(56,2)
obj2.ModularDivison(42,6)
obj2.Exponent(2,10)

#obj1 variables
obj1.obj = 'product1'
obj1.model_num = 324457
obj1.made_in = 'India'
obj1.color = 'Indigo'
obj1.discount = '10% Discount'


#obj2 variables
obj2.obj = 'product2'
obj2.model_num = 324458
obj2.made_in = 'China'
obj2.color = 'Purple'
obj2.discount = '20% Discount'


obj1.product_details()
obj2.product_details()


#Define Self?
#In Python, self is a special convention (not a keyword) used inside a class to represent the instance of the class itself.
# When you create an object from a class, self allows you to access and modify the attributes and methods that belong to that specific object.
