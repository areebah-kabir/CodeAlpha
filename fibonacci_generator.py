# The Fibonacci series is a sequence of numbers where each number is the sum of the two preceding ones, typically starting with 0 and 1. 
# Mathematically, it is defined by the recurrence relation:
# F(n)=F(n−1)+F(n−2)

def  fibonacci(n):
    fibonacci_series=[0,1]
    for i in range(2,n):
        next_value=fibonacci_series[i-1] + fibonacci_series[i-2]
        fibonacci_series.append(next_value)
    return fibonacci_series

print(fibonacci(71))
