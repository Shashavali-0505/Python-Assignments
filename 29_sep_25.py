
# reversing the string using recurssion-----------------------------------------------------------

def rev_str(str1):
    if len(str1) == 1:
        return str1

    return str1[-1] + rev_str(str1[: len(str1)-1])

str1 = 'bad morning'
print(rev_str(str1))

# multiply of two numbers without using * operator --------------------------------------------------------

def mul(m,n):
    if n == 1:
        return m
    
    if n == 0:
        return 0

    return m + mul(m,n-1)

print(mul(4,3))


# power of a number without using ** operator -------------------------------------------------------------

def mul(m,n):

    if m == 1:
        return 1
    
    if m == 0:
        return 1
    
    if n == 1:
        return m
    
    if n == 0:
        return 1

    return m * mul(m,n-1)

print(mul(4,1))


# reverse a list using recurssion-----------------------------------------------------

def rev_list(new_list):
    
    if len(new_list) == 0:
        return 'empty list is given'

    if len(new_list) == 1:
        return list2.append(new_list[0])

    return list2.append(new_list[-1]) , rev_list(new_list[ : len(new_list)-1])


list1 = [1,2,3,4,5]
list2 = []
rev_list(list1)
print(list2)
