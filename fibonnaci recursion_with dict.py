#finding fibonacci numbers using recursive function
import time
def fib(n):
    if n == 0:
        return 0
    
    elif n== 1 :
        return 1
    elif n == 2:
        return 1
    else:
        ans = fib(n-1)+ fib(n-2)
        return ans
import time
time1= time.time()
print(fib(4))
print(time.time()-time1)

