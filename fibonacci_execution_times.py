import time
import matplotlib.pyplot as plt

# Function to calculate Fibonacci numbers using recursion
def fibonacci_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) +fibonacci_recursive(n-2)
    
# Function to calculate Fibonacci numbers using dynamic programming
def fibonacci_dp(n):
    a = [None]*(n+1)
    a[0]= 0
    a[1] = 1

    for i in range(2,n+1):
        a[i] = a[i-1]+a[i-2]
    return a[n]

# Function to measure execution time for calculating Fibonacci numbers from F(1) to F(n)
def measure_execution_time(func, n):
    start_time = time.time()
    func(n)
    end_time = time.time()
    return (end_time - start_time)

# Task 1: Measure execution time for F(1) to F(100) using both methods
max_n = 100  # Variable to store the maximum value of n that can be computed within a reasonable time

n_values = list(range(1, max_n+1))
execution_times_recursive = []
execution_times_dynamic = []

for n in n_values:
    try:
        time_recursive = measure_execution_time(fibonacci_recursive, n)
        execution_times_recursive.append(time_recursive)
        print("time_recursive: %d: "%n, time_recursive)

        if time_recursive > 12*60*60:  # If time exceeds 12 hours
            execution_times_recursive.append(execution_times_recursive[n-1])
            print("Exceeded 12 hours at n =", n)
            max_n = n - 1
            print("Maximum value of n reached:", max_n)
            break

    except RecursionError:
        print("Recursion limit exceeded at n =", n)
        execution_times_recursive.append(execution_times_recursive[n-1])
        max_n = n - 1
        break

for n in n_values:
    time_dynamic = measure_execution_time(fibonacci_dp, n)
    execution_times_dynamic.append(time_dynamic)
    print("execution_times_dynamic: %d: "%n, time_dynamic)

# Plotting execution times
plt.plot(n_values, execution_times_recursive, label='Recursive')
plt.plot(n_values, execution_times_dynamic, label='Dynamic Programming')
plt.xlabel('n')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time of Fibonacci Calculation')
plt.legend()

plt.savefig('fibonacci_execution_time.png')
plt.show()
