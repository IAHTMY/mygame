
functions = ["**(1/2)", "3", "**2", "+", "5","o", " ", "7", "8", "9", "d", "c", 
             "4", "5", "6", "*", "/", "1", "2", "3", "+", "-", 
             "0", "00", " ", "a", "e"]

print(eval("".join(functions[1:5])))

obrazovka = "3-2"
answer = 0
def compute():
    for i in range(len(obrazovka)):
        if i == "*":
            if i+1 == "*" and i+2 == "2":
                answer += square(obrazovka[:i-1])
            else:
                answer += multiply(obrazovka[:i-1],  obrazovka[i:])
        elif i == "/":
            answer += divide(obrazovka[:i-1],  obrazovka[i:])
        elif i == "+":
            answer += add(obrazovka[:i-1],  obrazovka[i:]) 
        elif i == "-":
            answer += subtract(obrazovka[:i-1],  obrazovka[i:])
compute(obrazovka)
print(answer)

# Removing char at pos 3 
# using slice + concatenation 
obrazovka = "3-2"
for i in range(len(obrazovka)):
        answer = (obrazovka[:i-1] +  obrazovka[i:])