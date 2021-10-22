def sum_list(list):
    sum1 = 0
    for i in list:
        sum = i
        sum1 += i
    return sum1
list = [45 ,2, 10, -5, 100]
print(sum_list(list))