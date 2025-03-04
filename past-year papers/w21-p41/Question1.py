def Unknown(x, y):
    if x < y:
        print(x + y)
        return (Unknown(x + 1, y) * 2)
    else:
        if x == y:
            return 1
        else:
            print(x + y)
            return int(Unknown(x - 1, y) / 2)

def IterativeUnknown(x, y):
    result = 1
    while x < y:
        print(x + y)
        x = x + 1
        result = result * 2
    while x > y:
        print(x + y)
        x = x - 1
        result = int(result / 2)
    return result

a = 10
b = 15
print(a, b)
result1 = Unknown(a, b)
print(result1)
print(a, a)
result2 = Unknown(a, a)
print(result2)
print(b, a)
result3 = Unknown(b, a)
print(result3)
print(" ")
print(a, b)
result1 = IterativeUnknown(a, b)
print(result1)
print(a, a)
result2 = IterativeUnknown(a, a)
print(result2)
print(b, a)
result3 = IterativeUnknown(b, a)
print(result3)

