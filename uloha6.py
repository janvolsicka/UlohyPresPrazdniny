def my_function(start, end):
    sum_result = 0
    current_number = start
    while current_number <= end:
        sum_result += current_number ** 2
        current_number += 1
    return sum_result

print(my_function(1,10))