def print_rangoli(size):
	[print(''.join([chr(ord('a') + int(abs(((2*size - m) / 2 - 1)) + abs(n + 1 - size))) \
	if m % 2 == 0 and int(abs(((2*size - m) / 2 - 1)) + abs(n + 1 - size)) < size \
	else '-' for m in range(4*size - 3)])) for n in range(2*size - 1)]

if __name__ == '__main__':
	print_rangoli(int(input()))