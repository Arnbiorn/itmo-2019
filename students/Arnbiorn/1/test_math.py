def my_sum(first, secound):
    return first + secound

def my_mult(first, secound):
	return first * secound

def my_div(first, secound):
	return first / secound

def test_sum(): 
    assert my_sum(1, 2) == 3
    assert round(my_sum(2.1, 4.2),2) == 6.3

def test_mult():
	assert my_mult(-6, -4) == 24