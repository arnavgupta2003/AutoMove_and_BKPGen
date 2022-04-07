n = int(input())
	if(n<10):
		print(n-1)
	else:
		lst=[int(x) for x in str(n).split()]
		lst.sort()
		print(lst[-1]+1)