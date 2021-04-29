import re

def count_substring(string, sub_string):
	left = 0
	count = 0
	while True:
		match = re.search(sub_string, string[left:])
		if not match:
			break
		count += 1
		left += match.start() + 1
	return count

if __name__ == '__main__':
	string = input().strip()
	sub_string = input().strip()

	count = count_substring(string, sub_string)
	print(count)