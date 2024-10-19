#program to compute x ^ y without using math function
def comput_powr(x, y):
    result = 1
    while(y > 0):
        #if y is even,
        if (y % 2 == 0):
            x = x * x
            y >>= 1
        else:
            result = result * x
            y = y - 1
    return result
x = int(input("ENTER YOUR 1st NUMBER.."))
y = int(input("ENTER YOUR 2st NUMBER.."))
print("total", comput_powr(x, y))