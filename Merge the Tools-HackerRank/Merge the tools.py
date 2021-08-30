"""
    https://www.hackerrank.com/challenges/merge-the-tools/problem
             HACKERRANK
    Practice > Python > Strings > Merge the Tools!

------------------Athlete Sort---------------------
Sample Input

STDIN       Function
-----       --------
AABCAAADA   s = 'AABCAAADA'
3           k = 3


Sample Output

AB
CA
AD

"""
def merge_the_tools(string, k):
    str_list = []
    for i in string:
        str_list.append(i)
    new_list = []
    for i in range(0, len(str_list), k):
        new_list.append(str_list[i:i+k])
    print(new_list)
    for i in new_list:
        temp = []
        for j in i:
            if(j not in temp):
                temp.append(j)
        # print("".join(temp))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
