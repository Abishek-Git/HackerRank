"""
    https://www.hackerrank.com/challenges/input/problem
        HACKERRANK
    Practice > Python > Build-ins > input()

------------------input()---------------------

Input Format

The first line contains the space separated values of x and k.
The second line contains the polynomial P.

Output Format

Print True if O(x) = k. Otherwise, print False.

Sample Input

1 4
x**3 + x**2 + x + 1

Sample Output

True


"""
x, k = map(int, input().split())
print((True if(eval(input()) == k) else False))

