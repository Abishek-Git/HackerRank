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

