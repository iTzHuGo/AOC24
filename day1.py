def read_input(filename):
	with open(filename) as f:
		list1 = []
		list2 = []
		for line in f:
			a, b = line.split()
			list1.append(int(a))
			list2.append(int(b))
	return list1, list2


def total_distance(list1, list2):
	list1.sort()
	list2.sort()
	total_distance = 0
	for i in range(len(list1)):
		total_distance += abs(list1[i] - list2[i])
	return total_distance

def similiarity_score(list1, list2):
	similiarity_score = 0
	numbers = {}

	for i in list2:
		if i not in numbers:
			numbers[i] = 1
		else:
			numbers[i] += 1

	for i in list1:
		if i in numbers:
			sim_value = i * numbers[i]
			similiarity_score += sim_value

	return similiarity_score

if __name__ == '__main__':
	list1, list2 = read_input('day1_input.txt')
	print('Total distance: ', total_distance(list1, list2))
	print('Similiarity score: ', similiarity_score(list1, list2))