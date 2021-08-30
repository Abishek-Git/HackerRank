"""
    https://www.hackerrank.com/challenges/python-sort-sort/problem
             HACKERRANK
    Practice > Python > Build-ins > Athlete Sort

------------------Athlete Sort---------------------
You are given a spreadsheet that contains a list of N athletes and 
their details (such as age, height, weight and so on). You are 
required to sort the data based on the K th attribute and print the 
final resulting table. Follow the example given below for better 
understanding.

Input Format

The first line contains N and M separated by a space.
The next N lines each contain M elements.
The last line contains K.

Output Format

Print the K lines of the sorted table. Each line should contain the space 
separated elements. Check the sample below for clarity.


Sample Input 0

5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1


Sample Output 0

7 1 0
10 2 5
6 5 9
9 9 9
1 23 12

Explanation 0

The details are sorted based on the second attribute, since K is zero-indexed.

"""

N, M = map(int, input().split())
table = []
for _ in range(N):
    table.append(list(map(int, input().split())))
k = int(input())
sort_table = []
for item in table:
    sort_table.append(item[k])
sort_table.sort()
final_list = []
for value in sort_table:
    for item in table:
        if((item[k] == value) and item not in final_list):
            final_list.append(item)
            break

for item in final_list:
    for i in item:
        print(i, end=" ")
    print()
