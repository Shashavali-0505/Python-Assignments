#print the prime no's in given range btw 100 to2000

def check_isPrime(num):
    count = 1
    for j in range(2,num+1):
        if num % j == 0:
            count+=1
            if count > 2:
                break
    if count == 2:
        print(num,end=',')

start_num = int(input('enter starting number:'))
end_num = int(input('enter ending number:'))
for i in range(start_num,end_num+1):
    check_isPrime(i)


#print the Armstrong no's in given range btw 100 to2000

def check_isArmstrong(num):
    sum = 0
    # length_of_number = len(str(num))
    n0_of_digits = 0
    length = num
    while length > 0:
        n0_of_digits+=1
        length = length // 10
    temp = num
    while temp > 0:
        reslt = temp % 10
        sum = (sum + (reslt ** n0_of_digits))
        temp = temp // 10

    if num == sum: print(f'{num} is a Armstrong number')

st_number = int(input('enter the starting number:'))
end_number = int(input('enter the ending number:'))
for k in range(st_number,end_number+1):
    check_isArmstrong(k)


