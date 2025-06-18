
functions = ["**(1/2)", "3", "**2", "+", "5","o", " ", "7", "8", "9", "d", "c", 
             "4", "5", "6", "*", "/", "1", "2", "3", "+", "-", 
             "0", "00", " ", "a", "e"]
"""
print(eval("".join(functions[1:5])))

a = [1, 2, 3, 4]

print(a[3])"""
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# Removing char at pos 3 
# using slice + concatenation 
obrazovka = "3-2"
for i in range(len(obrazovka)):
    if i == "-":
        answer = subtract(obrazovka[:i-1],  obrazovka[i:])

    


