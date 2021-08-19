"""
Given the participants' score sheet for your University Sports Day,
you are required to find the runner-up score. You are given  scores.
Store them in a list and find the score of the runner-up.

"""

total = int(input())
marks = list(map(int, input().split()))
marks.sort()

runner = 0
for i in marks[::-1]:
    if(i < marks[-1]):
        runner = i
        break

print(i)
