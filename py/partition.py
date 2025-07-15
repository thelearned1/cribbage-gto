def iter_partitions (lst):
	partition_count = 2**len(lst)
	for number in range(partition_count):
		iteration = []
		curr = number 
		idx = 0
		while curr > 0:
			if curr % 2: 
				iteration.append(lst[idx])
			curr = curr // 2
			idx+=1
		yield iteration