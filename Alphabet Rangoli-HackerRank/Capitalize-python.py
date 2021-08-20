"""
            Alphabet Rangoli

https://www.hackerrank.com/challenges/alphabet-rangoli/problem

You are given an integer,N . Your task is to print an 
alphabet rangoli of size N. (Rangoli is a form of Indian
 folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

#size 10

------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------


"""

from string import ascii_lowercase

def print_rangoli(N):
    case = list(ascii_lowercase)
    height = (N * 2 - 1)
    width = height * 2 -1

    alpha = [case[N-1]]
    for i in range(1, N):
        alpha += [alpha[i-1][:i] + case[N-i-1] + alpha[i-1][:i][::-1]]

    final = alpha
    for item in range(len(alpha)-2, -1, -1):
        final += [alpha[item]] 

    for s in final:
        print("-".join(list(s)).center(width, "-"))

    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)