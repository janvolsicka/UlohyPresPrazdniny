def my_function(number):
    if number<0:
        return ("Číslo je záporné.")
    elif number>0:
        return("Číslo je kladné")
    else:
        return("Číslo není ani kladné, ani záporné.")
    
funkce=my_function(-36)
print(funkce)