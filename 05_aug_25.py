#if and else problems
#1.checking the given number is positive / negative/zero---------------------------------------------------------------------------------------------
def num_checking(a):
    if num > 0:
        print('positive')
    elif num == 0:
        print('zero')
    else:
        print('negative')

num = int(input('enter a number:'))
num_checking(num)

#2.checking the given no even / odd----------------------------------------------------------------------------------------------------------------
#using terinary operator
def even_or_odd (num1):
    res = 'even' if num1  % 2 == 0 else 'odd'
    print(res)

even_or_odd(23)

#3.checking he given age >=18 using terinary operator----------------------------------------------------------------------------------------------
def checking_age(age):
    res = 'eligible' if age>= 18 else 'not eligible'
    print(res)

num2 = int(input('enter your age'))
checking_age(num2)

#4.checking the given two numbers which is greater using 2 terinary operators-----------------------------------------------------------------------
def greater_of_two_numb(a,b):
    res = f'{a},{b} both are equal' if a==b else f'{a} is greater' if a > b  else f'{b} is greater'
    print(res)

greater_of_two_numb(23,65)


#5.Print "Pass" if a student scores more than 40 marks;otherwise, print "Fail."-------------------------------------------------------------------
def student_result(marks):
    return 'Pass' if marks >= 40 else 'Fail'

st_marks = int(input('enter your marks:'))
result = student_result(st_marks)
print(f'you have {result} the exam.....')

#6.Write a program to display the day of the week based on a number input (1 for Monday, 2 for Tuesday, etc.).-------------------------------------

def display_week(num_week):
    if num_week == 1:
        return 'Monday'
    elif num_week == 2:
        return 'Tuesday'
    elif num_week == 3:
        return 'Wednesday'
    elif num_week == 4:
        return 'Thursday'
    elif num_week == 5:
        return 'Friday'
    elif num_week == 6:
        return 'Saturday'
    elif num_week == 7:
        return 'Sunday'
    else:
        return 'Invalid input check once....'
    

week_num = int(input('enter your week no:'))
week_res = display_week(week_num)
print(week_res)


#7.Implement a simple calculator to perform addition, subtraction, multiplication, and division.

def simple_calculator(num1,num2,oper):
    if oper in ['+','add']:
        return num1 + num2
    elif oper in ['-','sub']:
        return num1 - num2
    elif oper in ['*','mul']:
        return num1 * num2
    elif oper in ['/','div']:
        return 'divison by zero is not possible'  if num2 == 0 else num1 / num2
    else:
        return 'invalid input'
         
a = float(input('enter first number:'))
b = float(input('enter second number:'))
input_operator = input('enter a operator').lower()
res = simple_calculator(a,b,input_operator)
print(res)

#8.Write a program to display the name of a month based on the month number (1 for January, 2 for February, etc.).

def display_month(num_month):
    if num_month == 1:
        return 'January'
    elif num_month == 2:
        return 'February'
    elif num_month == 3:
        return 'March'
    elif num_month == 4:
        return 'April'
    elif num_month == 5:
        return 'May'
    elif num_month == 6:
        return 'June'
    elif num_month == 7:
        return 'July'
    elif num_month == 8:
        return 'August'
    elif num_month == 9:
        return 'September'
    elif num_month == 10:
        return 'october'
    elif num_month == 11:
        return 'November'
    elif num_month == 12:
        return 'December'
    else:
        return 'Invalid input check once....'

month_num = int(input('enter your month no:'))
month_res = display_month(month_num)
print(month_res)


#1.Write a program to find the greatest of three numbers.

def checking_greter_no(a,b,c):
    return f'{a} is greater' if a > b > c else f'{b} is greater' if a < b > c else f'{c} is greater'

num1 = int(input('enter the number:'))
num2 = int(input('enter the number:'))
num3 = int(input('enter the number:'))
result = checking_greter_no(num1,num2,num3)
print(result)


#2.Check if a year is a leap year.

def check_leap_year(year):
    if year < 0:
        return 'invalid year'
    return 'leap year' if (year % 400 == 0) or (year % 4 == 0 and year % 100 !=0) else 'not a leap year' 

year = int(input('enter the year:'))
checked = check_leap_year(year)
print(checked)


#3.Write a program to classify a character entered by the user as a vowel, consonant, or neither.

def type_of_char(str1):
    if str1 in ['a','e','i','o','u']:
        return 'vowel'
    return 'consonant'

char1 = input('enter only single character:').lower()
check = type_of_char(char1)
print(check)


#4.Calculate the grade of a student based on the marks they
# score:
# 1. 90-100: Grade A
# 2. 80-89: Grade B
# 3. 70-79: Grade C
# 4. <70: Fail.

def st_results_check(marks):
    return 'Grade A' if marks >= 90 else 'Grade B' if marks >= 80 else 'Grade C' if marks >= 70 else 'Fail'

st_marks = int(input('enter your marks:'))
result = st_results_check(st_marks)
print(result)