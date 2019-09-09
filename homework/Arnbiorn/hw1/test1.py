def filter_empty(sequence):
	return list(filter(
		lambda string: len(string), 
		sequence
	))

def test_delete():
	assert filter_empty([]) == []
	assert filter_empty(['']) == []
	assert filter_empty(['','']) == []
	assert filter_empty(['a', '']) == ['a']
	assert filter_empty(['a','b']) == ['a','b']

if __name__=='__main__':
	test_delete()


# if __name__ == '__main__':
# 	main()
# 	tests = [
# 		globals()[variable]
# 		for variable in globals()
# 		if variable.startswith('test_')
# 		]

# 	for test in tests:
# 		try:
# 			test()
# 		except AssertionError:
# 			print('Failed test: ', test.__name__)
# 			raise