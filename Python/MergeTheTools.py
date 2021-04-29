from collections import OrderedDict

def merge_the_tools(string, k):
	print('\n'.join([''.join(OrderedDict.fromkeys(let)) for let in [string[i:i + k] for i in range(0, len(string), k)]]))

if __name__ == '__main__':
	string, k = input(), int(input())
	merge_the_tools(string, k)