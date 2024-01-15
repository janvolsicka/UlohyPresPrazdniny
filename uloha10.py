def my_function(veta):
    y = 1
    for x in veta:
        if x == " ":
            y+=1
    return y

text = ("Jakub nemá rád školu, proto si užívá prázdniny.")
print(my_function(text))