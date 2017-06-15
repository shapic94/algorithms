import time
# KMP Algorithm
def kmp(t, p):
	time_start = time.time()
	index = []
	j = 0
	i = 0
	while i < len(t):
		if t[i] == p[j]:
			i = i + 1
			j = j + 1
		else:
			i = i + 1

		if j >= len(p):
			j = 0
			index.append(i - len(p))
			i = i - len(p) + 1

	return index, str(format(time.time() - time_start, '.10f'))



t = ['A', 'A', 'B', 'A', 'A', 'C', 'A', 'A', 'D', 'A', 'A', 'B', 'A', 'A', 'B', 'A']
p = ['A', 'A', 'B', 'A']
find = kmp(t, p)
print('Pattern je pronadjen na indexima {}, za vreme {}'.format(find[0], find[1]))

t = ['T', 'H', 'I', 'S', ' ', 'I', 'S', ' ', 'A', ' ', 'T', 'E', 'S', 'T', ' ', 'T', 'E', 'X', 'T']
p = ['T', 'E', 'S', 'T']
find = kmp(t, p)
print('Pattern je pronadjen na indexima {}, za vreme {}'.format(find[0], find[1]))


# Rabin-Karp Algorithm
def hash(s):
	prime = 3
	result = 0
	for i in range(len(s)):
		if i == 0:
			result = + (ord(s[i]) - ord('A') + 1)
		else:
			result = result + (ord(s[i]) - ord('A') + 1)*pow(prime, i)
	return result

def rk(t, p):
	time_start = time.time()
	index = []
	i = 0
	hp = hash(p)
	while i < len(t):
		if len(t) - i >= len(p):
			# First check [hash]
			if hp == hash(t[i:len(p)+i]):
				# Second check [values]
				j = 0
				isReal = True
				for j in range(len(p)):
					if p[j] != t[i+j]:
						isReal = False
						break
				if isReal:
					index.append(i)
			i = i + 1
		else:
			break
	return index, str(format(time.time() - time_start, '.10f'))

t = ['A', 'A', 'B', 'A', 'A', 'C', 'A', 'A', 'D', 'A', 'A', 'B', 'A', 'A', 'B', 'A']
p = ['A', 'A', 'B', 'A']
find = rk(t, p)
print('Pattern je pronadjen na indexima {}, za vreme {}'.format(find[0], find[1]))


t = ['T', 'H', 'I', 'S', ' ', 'I', 'S', ' ', 'A', ' ', 'T', 'E', 'S', 'T', ' ', 'T', 'E', 'X', 'T']
p = ['T', 'E', 'S', 'T']
find = rk(t, p)
print('Pattern je pronadjen na indexima {}, za vreme {}'.format(find[0], find[1]))


# test = 'a'
# test1 = (ord(test) - ord('A') + 1) + 1
# print(test1)