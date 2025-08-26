#Fibinocci series-----------------------------------------------------
series = int(input('enter the end of the series:')) #using while loop
n1 , n2 = 0 , 1
while series > 0:
    print(n1)
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    series-=1

series = int(input('enter the end of the series:')) #using for loop
n1 , n2 = 0 , 1
for i in range(series):
    print(n1)
    n3 = n1 + n2
    n1 = n2
    n2 = n3

#Armstrong number-----------------------------------------------------------
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


#Armstrong number in given range between
number = int(input('enter the number:'))
for i in range(1,number+1):
    temp = i
    sum = 0
    length_of_number = len(str(i))
    while temp > 0:
        reslt = temp % 10
        sum = (sum + (reslt ** length_of_number))
        temp = temp // 10

    if i == sum: print(f'{i} is a Armstrong number')




