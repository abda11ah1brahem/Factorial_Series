import math
def series_sum(x):
    sum = 1
    for i in range(2, x+1):
        if i % 2 == 0:
            sum += 1 / math.factorial(i)
        else:
            sum -= 1 / math.factorial(i)
    return sum

x = int(input("Enter the value of x: "))
print("The sum of the series is:", series_sum(x))