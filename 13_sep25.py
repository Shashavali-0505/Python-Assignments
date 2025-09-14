# List problems
# finding the index element in the list
def index_element(input_list,input_index):

    if input_index < -len(input_list) or input_index > len(input_list)-1:
        return 'Invalid index'

    return input_list[input_index]



list1 = [1,2,34,5,6,7,45]
index = int(input('enter your index num:'))

print(index_element(list1,index))
#-----------------------------------------------------------------------------------------------------

#find the sum,max,min in list
#using sort method

def list_checking(ip_list):
    if len(ip_list) == 0:
        return 'empty list'
    
    sum = 0
    for i in ip_list:
        sum += i
    
    ip_list.sort()
    return f'sum:{sum},max:{ip_list[-1]},min:{ip_list[0]}'

list3 = [87,33,22,66,98,2,43,54]
print(list_checking(list3))

#using for loop
def list_sum_max_min_op(ip_list):

    if ip_list == []:
        return 'empty list'
    
    sum = 0
    max_elem = ip_list[0]
    min_elem = ip_list[0]

    for i in ip_list:
        sum += i
        if i > max_elem:
            max_elem = i

        if i < min_elem:
            min_elem = i

    return f'sum:{sum},max:{max_elem},min:{min_elem}'

list2 = [45,22,32,66,7,-87,45,56]
print(list_sum_max_min_op(list2))
#---------------------------------------------------------------------------------------------------------------

    