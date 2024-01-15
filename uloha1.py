text=["mrakodrap"]
v = "a"

def my_function(y,text):
    a=0
    for x in text:
        while x == y:
            a += 1
    return a

print(my_function(v,text))