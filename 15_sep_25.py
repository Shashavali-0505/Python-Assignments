#1.String Reverse 
#method1 (reverse())

str1 = 'Shashavali'
str1.reverse() #AttributeError: 'str' object has no attribute 'reverse'
print(str1)

#method2 (slicing)

str2 = 'Shashavali'
# print(str2[::-1]) # here string will be reversed but not reflected to the main string , in order to change the input string to reverse we use re-assignment to that variable.
str2 = str2[: : -1]
print(str2)

#method3 (with empty string)
str3 = 'Shashavali'
new_str1 = ''
for i in range(len(str3)):
    # print(i)
    # print(str3[i])
    new_str1 = str3[i] #we can not add elements/characters to a string once it is fixed (item assign is not possible) 
print(new_str1)
    

#method4 (swaping)

str4 = 'Shashavali'
low = 0
high = len(str4) - 1
while low < high:
    str4[low],str4[high] = str4[high],str4[low] #TypeError: 'str' object does not support item assignment
    low += 1
    high -= 1

print(str4)


#2.Sum of digits of each number in the given list. Output should be in list format

def sum_of_list_in_numbers(ip_list):
    new_list2 = []
    for i in ip_list:
        sum = 0
        str1 = str(i)
        for j in str1:
            sum += int(j)
        new_list2.append(sum)

    return f'old-list:{ip_list},new-sum-list:{new_list2}'

list5 = [12,434,7865,60,6790]
print(sum_of_list_in_numbers(list5))

#3.Find max digit in the given number

def maxDigit_in_given_number(number):
    max_digit = 0
    temp = number
    while temp > 0:
        one_digit = temp % 10
        if one_digit > max_digit:
            max_digit = one_digit
        temp = temp // 10
    
    return f'the maximum digit in the given number is:{number},{max_digit}'



num1 = int(input('enter your number:'))
print(maxDigit_in_given_number(num1))

#4.Find max digit for every number in the given list


def maxDigit_in_given_number(ip_list):
    new_lits3 = []
    for i in ip_list:
        max_digit = 0
        temp = i
        while temp > 0:
            one_digit = temp % 10
            if one_digit > max_digit:
                max_digit = one_digit
            temp = temp // 10
        
        new_lits3.append(max_digit)
    
    return f'the maximum digit in the given list_numbers is:{ip_list},{new_lits3}'


list6 = [123,456,789,6573]
print(maxDigit_in_given_number(list6))