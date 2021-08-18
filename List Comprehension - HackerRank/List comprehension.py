"""
Let's learn about list comprehensions! You are given three integers
x, y and z representing the dimensions of a cuboid along with an 
integer n. Print a list of all possible coordinates given by(i, j, k)
on a 3D grid where the sum of i+j+k is not equal to n.
Here 0<=i<=x, 0<=j<=y, 0<=k<=z Please use list comprehensions rather
than multiple loops, as a learning exercise.

"""





from itertools import combinations
def combine(i, j, k, n):
    return([[x,y,z] for x in range(i+1) for y in range(j+1) for z in range(k+1) if((x+y+z) != n)])


if __name__ == '__main__':
    i = int(input())
    j = int(input())
    k = int(input())
    n = int(input())
    print(combine(i, j, k, n))
