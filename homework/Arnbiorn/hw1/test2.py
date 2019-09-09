def is_possitive(input_function=input):
	return int(input_function('Your number: ')) > 0

def test_is_positive():
	assert is_possitive(lambda _: 1)
	assert is_possitive(lambda _: -1) is False

	try:
		assert is_possitive(lambda _: 'a')
	except ValueError:
		assert True
	else:
		assert False

if __name__ == '__main__':
	test_is_positive()

# if __name__ == '__main__':
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