"""
You are asked to ensure that the first and last names of
people begin with a capital letter in their passports.
For example, alison heck should be capitalised correctly as Alison Heck.

alison heck ------>  Alison Heck
"""

def solve(s):
    list = s
    s = []
    for i in list:
        s.append(i)
    s[0] = s[0].capitalize()
    for i in range(len(s)):
        if(s[i-1] == " "):
            s[i] = s[i].capitalize() 

    return "".join(s)
    

if __name__ == '__main__':
    name = input()
    print(solve(name))
