#reversing a number
#Ex: 123 O/P: 321

num = int(input('enter your number:'))
temp = num
rev_num = 0
while temp > 0:
    one_num = temp % 10
    # print(one_num,end='') #1
    rev_num = rev_num * 10 + one_num #2
    temp = temp // 10
print(rev_num)


#palindrome number
#Ex: 515 O/P: 515

num1 = int(input('enter your number:'))
temp1 = num1
num_rev = 0
while temp1 > 0:
    digits = temp1 % 10
    num_rev = num_rev * 10 + digits
    temp1 //= 10
if num_rev == num1: print(f'{num1} is a palindrome number')
else: print(f'{num1} is not a palindrome number')


#In a given number print only the even no's Ex: 5642830 O/P: 6,4,2,8,0

num2 = int(input('enter your number:'))
while num2 > 0:
    digit = num2 % 10
    if digit % 2 == 0:
        print(digit,end=',')
    num2 = num2 // 10

#In a given number print only the prime no's Ex: 5642830 O/P: 5,2,3

num3 = int(input('enter your number:'))
while num3 > 0:
    digit = num3 % 10
    if digit in [2,3,5,7]:
        print(digit,end=',')
    num3 = num3 // 10

#To print the given number is a perfect number or not
#Ex: num = 6 is a perfect number , factors=1,2,3 if sum of the factors is equal to given number then it is a perfect number

num4 = int(input('enter a number:'))
sum = 0
for i in range(1,num4):
    if num4 % i == 0:
        sum+=i
if sum == num4:
    print(f'{num4} is a perfect number')
else:
    print(f'{num4} is not a perfect number')

#same in between range from 1 to 100 print all perfect number

def check_perfect_no(number):
    sum = 0
    for i in range(1,number):
        if number % i == 0:
            sum+=i
    if sum == number:
        print(f'{number} is a perfect number')


st_num = int(input('enter starting number:'))
end_num = int(input('enter last number:'))
for i in range(st_num,end_num+1):
    check_perfect_no(i)
    