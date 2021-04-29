if __name__ == '__main__':
	N = int(input())
	mylist = []
	for i in range(N):
		order = list(input().split())
		if(order[0] == 'print'):
			print(mylist)
		elif(order[0] == 'sort'):
			mylist.sort()
		elif(order[0] == 'pop'):
			mylist.pop()
		elif(order[0] == 'reverse'):
			mylist.reverse()
		elif(order[0] == 'append'):
			mylist.append(int(order[1]))
		elif(order[0] == 'remove'):
			mylist.remove(int(order[1]))
		elif(order[0] == 'insert'):
			mylist.insert(int(order[1]), int(order[2]))