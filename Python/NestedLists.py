if __name__ == '__main__':
	mylist = []
	for _ in range(int(input())):
		student = [input(), float(input())]
		mylist.append(student)

	score_list = list(set([x[1] for x in mylist]))
	score_list.sort()
	ans = []
	for student in mylist:
		if(score_list[1] == student[1]):
			ans.append(student[0])
	ans.sort()
	print(*ans, sep='\n')