import timeit
p = timeit.default_timer()
q = timeit.default_timer()
#for i in range(10000):
while q - p < 5:
	q = timeit.default_timer()
	#if q - p > 15:
	#	break
print("Would you like inspiration?")
