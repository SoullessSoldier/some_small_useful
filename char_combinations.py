import itertools
a="quick"
'''
У permutations 2 параметра - откуда брать и по сколько символов группировать, т.е пример ниже переберет все перестановки целиком quick, quikc, qucik и тд,
а если permutations(a,2), то будут группы по 2 символа - qu, qi, qc и тд
'''
for i in list(itertools.permutations(a)):
	print(''.join(i))
    
