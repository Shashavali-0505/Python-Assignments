num = int(input('enter the number:'))
sum = 0
length_of_number = len(str(num))
temp = num
while temp > 0:
    reslt = temp % 10
    sum = (sum + (reslt ** length_of_number))
    temp = temp // 10

if num == sum: print(f'{num} is a Armstrong number')
else: print(f'{num} is not a Armstrong number')