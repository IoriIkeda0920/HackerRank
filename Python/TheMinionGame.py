import re

def minion_game(string):
	ans = {'Stuart':0, 'Kevin':0}
	n = len(string)

	ans['Kevin'] = int(sum([n - int(m.start()) for m in re.finditer('A|E|I|O|U', string)]))
	ans['Stuart'] = int(n*(n + 1) / 2 - ans['Kevin'])
	if(ans['Kevin'] == ans['Stuart']):
		print('Draw')
		return
	print(*list((max(ans.items(), key=lambda x: x[1]))))

if __name__ == '__main__':
	s = input()
	minion_game(s)