import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
	return ' '.join(word.capitalize() for word in re.split(' ', s))

if __name__ == '__main__':
	s = input()

	result = solve(s)

	print(result)
