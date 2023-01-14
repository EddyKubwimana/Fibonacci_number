# Fibonacci_number
In this repository, I tried to find the nth fibonnaci numbers using two method: Iterative solution and recursive function

# Recursive solution:
I used the recursive function to find the nth number but the problem with this is that for each function call, it adds a  new stack with may take a much resources

# iterative implementation:

using the iterative implementation, I used the concept of memoization (https://www.geeksforgeeks.org/memoization-using-decorators-in-python)to make sure that if we have the previous result are stored to speed up calculation of nth fibonacci number

# Comparison between the recursive solution and iterative solution:
An iterative solution to finding a Fibonacci number in Python would involve using a loop to iterate through the sequence and calculate the next number in the series. This can be implemented using a for loop or a while loop. The time complexity of this method is O(n), where n is the position of the Fibonacci number in the sequence. The space complexity is O(1), as only a single variable is needed to store the current number in the sequence.

A recursive solution to finding a Fibonacci number in Python would involve calling the same function repeatedly with different input values, until the base case is reached. The time complexity of this method is O(2^n), as for each recursive call, 2 additional calls are made, and space complexity is O(n) as function call stack need to store n function calls.

In terms of best case use, an iterative solution is generally faster and more memory-efficient for large values of n.
Recursive solution is best suited for smaller values of n and when the recursive call tree is smaller (e.g. for small inputs) or when the problem has overlapping subproblems.

In general, for large inputs, iterative solution is preferable over recursive solution because of the large overhead of recursive calls.
