import time
def fib(n):
    if n ==1 or n == 0:
        return 1
    else:
        return fib(n-1)+ fib(n-2)

time1= time.time()
print(fib(40))
print(time.time()- time1)


