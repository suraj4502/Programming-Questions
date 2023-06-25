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
    for i in range(2, int(sqrt(N)) +1 ):   #if num is 25 then it checks if it is divisible by 2,3,4,5
        if N % i == 0:
            return False
    return True


if __name__ == "__main__":
    n = int(input("Enter the number :"))
    ans = isPrime(n)
    if n != 1 and ans == True:
        print("Prime Number")
    else:
        print("Non Prime Number")