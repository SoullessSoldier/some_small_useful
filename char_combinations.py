import itertools
a="quick"
for i in list(itertools.permutations(a)):
	print(''.join(i))
    
