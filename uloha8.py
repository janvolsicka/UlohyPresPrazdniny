def my_function(numbers=(13,58,158,2,-3)):
    y=0
    for x in numbers:
        if x>y:
            y=x
    return y

print(my_function())