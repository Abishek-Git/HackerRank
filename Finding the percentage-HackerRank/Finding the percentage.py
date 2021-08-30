"""
			HACKERRANK
        https://www.hackerrank.com/challenges/finding-the-percentage/problem

        Practice > PythonBasic > Data Types > Finding the percentage
        
The provided code stub will read in a dictionary containing key/value
pairs of name:[marks] for a list of students. Print the average of the 
marks array for the student name provided, showing 2 places after the 
decimal.


Sample Input 0

    3
    Krishna 67 68 69
    Arjun 70 98 63
    Malika 52 56 60
    Malika

Sample Output 0

    56.00


Sample Input 1

    2
    Harsh 25 26.5 28
    Anurag 26 28 30
    Harsh

Sample Output 1

    26.50

"""

def average(new_dict, name):
	return sum(new_dict.get(name))/len(new_dict.get(name))


if __name__ == '__main__':
	n = int(input())
	new_dict = {}
	for _ in range(n):
		key, *value = input().split()
		temp_list = list(map(float, value))
		new_dict[key] = temp_list
	name = input()
	print("{:.2f}".format(average(new_dict, name)))

