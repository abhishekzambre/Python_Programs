def factorial(n):
	"""Factorial function"""
	return 1 if n == 0 else n * factorial(n-1)


def draw_line(tick_length, tick_label=''):
	"""Draw one line with given tick length"""
	line = '-'*tick_length
	if tick_label:
		line += ''+tick_label
	print(line)

def draw_interval(center_length):
	"""Draw tick interval based upon a central tick length"""
	if center_length > 0:
		draw_interval(center_length-1)
		draw_line(center_length)
		draw_interval(center_length-1)

def draw_ruler(num_inches, major_length):
	"""Draw English ruler with given number of inches, major tick length"""
	draw_line(major_length, '0')
	for j in range(1, 1+num_inches):
		draw_interval(major_length-1)
		draw_line(major_length, str(j))

def binary_search(data, target, low, high):
	"""Binary search using recursion"""
	if low>high:
		return False
	else:
		#mid = (high-low) // 2 + low
		mid = (low+high) >> 1
		if target == data[mid]:
			return True
		elif target < data[mid]:
			return binary_search(data, target, low, mid-1)
		else:
			return binary_search(data, target, mid+1, high)



print("factorial(5) =",factorial(5))
print("factorial(10) =",factorial(10))


draw_ruler(3, 2)

data = [1,3,6,8,9,10,25,47,60]

print('Is 10 present?', binary_search(data, 10, 0, len(data)-1))
print('Is 60 present?', binary_search(data, 60, 0, len(data)-1))
print('Is 14 present?', binary_search(data, 14, 0, len(data)-1))
print('Is 0 present?', binary_search(data, 0, 0, len(data)-1))