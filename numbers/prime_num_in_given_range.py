

def isPrime(N):
    if N <= 1:
        return False
    for i in range(2, (N**0.5)+1):
        if N % i == 0:
            return False
        return True
    
def isPrime(N):
    # Check if the number is less than or equal to 1
    if N <= 1:
        return False

    # Iterate from 2 to the square root of N
    # We only need to check divisibility up to the square root of N because
    # if N is divisible by any number greater than its square root, then it
    # would also be divisible by a smaller number.
    for i in range(2, int(N**0.5) + 1):
        # If N is divisible by i, it is not a prime number
        if N % i == 0:
            return False

    # If the number is not divisible by any number in the range,
    # then it is a prime number
    return True



def find_prime_numbers(n):
    list_of_prime_numbers = [1]
    
    for i in range(2,n+1):
        if isPrime(i):
            list_of_prime_numbers.append(i)
            
    return list_of_prime_numbers



if __name__ == "__main__":
    n = int(input("Enter the Range in which you want to find the prime numbers : "))
    print(find_prime_numbers(n))

        
    