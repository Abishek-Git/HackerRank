from itertools import combinations
def combine(i, j, k, n):
    return([[x,y,z] for x in range(i+1) for y in range(j+1) for z in range(k+1) if((x+y+z) != n)])



if __name__ == '__main__':
    i = int(input())
    j = int(input())
    k = int(input())
    n = int(input())
    print(combine(i, j, k, n))