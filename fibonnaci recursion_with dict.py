#utilazation of memoization concept
import time
def fib(n, d = {0:0, 1:1, 2:1}):

    
    if n in d:
        return d[n]
    else:
        ans = fib(n-1,d)+ fib(n-2,d)
        d[n] = ans
        return ans
import time
time1= time.time()
print(fib(1000))
print(time.time()-time1)

