def my_function(temperatures=(13,12,15,14,16,18,20)):
    avrg_temperature=0
    for x in temperatures:
        avrg_temperature+=x
    avrg_temperature=avrg_temperature/7
    return avrg_temperature

print(my_function())