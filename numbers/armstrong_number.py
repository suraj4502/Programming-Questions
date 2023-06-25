'''
Problem Statement: Given a number, check if it is Armstrong Number or Not.

Examples:

Example 1:
Input:153 
Output: Yes, it is an Armstrong Number
Explanation: 1^3 + 5^3 + 3^3 = 153

Input:170 
Output: No, it is not an Armstrong Number
Explanation: 1^3 + 7^3 + 0^3 != 170
What are Armstrong Numbers?

Armstrong Numbers are the numbers having the sum of digits raised to power no. of digits is 
equal to a given number.
Examples- 0, 1, 153, 370, 371, 407, and 1634 are some of the Armstrong Numbers.
'''




def isArmstrongNumber(n):
    og_number = n
    power = len(str(n))
    sum = 0
    
    while n > 0:
        right_most_digit = n%10  
        '''
        if n is 153, then digit = 153 % 10 gives the remainder 3, which is the rightmost digit.
        This is because when you divide 153 by 10, you get 15 as the quotient and 3 as the remainder.
        '''
        sum += right_most_digit**power
        n = n//10  
        '''
        n is divided by 10 using the floor division operator //. 
        This removes the rightmost digit from n and updates its value.
        For example, if n is 153, then n //= 10 gives the quotient 15, 
        effectively removing the rightmost digit (3) from n.
        '''

    return sum == og_number


if __name__ =="__main__":
    number = int(input("Enter the number to Check if it an armstong number or not : "))
    print(f"Modulo operator(gives reamainder) with 10 to get the rightmost number which is : {number%10} ")
    print(f"Floor division(rounds the result with nearest whole number) with 10 to remove the rightmost number which is : {number//10}")
    print("Result ==> ")
    if isArmstrongNumber(number):
        print("Yes, it is an Armstrong Number")
    else:
        print("No, it is not an Armstrong Number")
    
