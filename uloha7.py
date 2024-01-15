def my_function(word="tři sta třicet tři"):
    y = 0
    for x in word:
        if x == "ř":
            y+=1
    return y

print(my_function())