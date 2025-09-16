# 1.Bubble sorting(Can you wrtie bubble sort for decending order)

#ascending order
def bubble_sorting(ip_list):

    for j in range(0,len(ip_list)):
        for i in range(0,len(ip_list)-1-j):
            if ip_list[i] > ip_list[i+1]:
                ip_list[i],ip_list[i+1] = ip_list[i+1],ip_list[i]

    return ip_list

List1 = [36,81,44,9,-1,2,64,-5]
print(bubble_sorting(List1))

#descending order
def bubble_sorting(ip_list):

    for j in range(0,len(ip_list)):
        for i in range(0,len(ip_list)-1-j):
            if ip_list[i] < ip_list[i+1]:
                ip_list[i],ip_list[i+1] = ip_list[i+1],ip_list[i]

    return ip_list

List1 = [36,81,44,9,-1,2,64,-5]
print(bubble_sorting(List1))


# 2.Use bubble sort to sort strings => How will you get the output Use bubble sort to sort strings based on their lengths. That is strings with highest length should go to last

def bubble_string_sort(ip_list):

    for i in range(0,len(ip_list)):
        for j in range(0,len(ip_list)-1-i):
            if len(ip_list[j]) > len(ip_list[j+1]):
                ip_list[j],ip_list[j+1] = ip_list[j+1],ip_list[j]

    return ip_list


List2 = ['apple','elephant','banana','cat','to','swim']
print(bubble_string_sort(List2))


#3.Can you sort nested lists based on the first element of each nested list.

def bubble_sort_nested_list(ip_list):

    for j in range(len(ip_list)):
        for i in range(0,len(ip_list)-1-j):
            if ip_list[i][0] > ip_list[i+1][0]:
                ip_list[i],ip_list[i+1] = ip_list[i+1],ip_list[i] 

    return ip_list

List3 = [[45,675,34],[565,4,999],[78,876,0],[990],[10,78,556,565],[129,44,99,62,12345],[665,9,242,789,987],[0,7876,0,9887]]
print(bubble_sort_nested_list(List3))