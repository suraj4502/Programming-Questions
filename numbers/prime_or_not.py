'''
Problem Statement: Given a number, check whether it is prime or not. A prime number is a natural number that is only divisible by 1 and by itself.

Examples 1 2 3 5 7 11 13 17 19 …

Examples
Example 1:
Input: N = 3
Output: Prime
Explanation: 3 is a prime number

Example 2:
Input: N = 26
Output: Non-Prime
Explanation: 26 is not prime
'''

from math import sqrt

def isPrime(N):
    # Check if the number is less than or equal to 1
    if N <= 1:
        return False

    # Iterate from 2 to the square root of N
    # We only need to check divisibility up to the square root of N because
    # if N is divisible by any number greater than its square root, then it
    # would also be divisible by a smaller number.
    for i in range(2, sqrt(N) + 1):
        # If N is divisible by i, it is not a prime number
        if N % i == 0:
            return False

    # If the number is not divisible by any number in the range,
    # then it is a prime number
    return True

if __name__ == "__main__":
    n = int(input("Enter the number :"))
    ans = isPrime(n)
    if n != 1 and ans == True:
        print("Prime Number")
    else:
        print("Non Prime Number")