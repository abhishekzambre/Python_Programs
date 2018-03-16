import os

def disk_usage2(path):
	total = os.path.getsize(path)
	if os.path.isdir(path):
		for f in os.listdir(path):
			c = os.path.join(path,f)
			total += disk_usage(c)
	return total

def disk_usage(path):
	"""Return no. of bytes used by a file/folder and any descendents."""
	total = os.path.getsize(path)
	if os.path.isdir(path):
		for filename in os.listdir(path):
			childpath = os.path.join(path, filename)
			total += disk_usage(childpath)
	print('{0:<9}'.format(total),path)
	return total

print(disk_usage("/Users/abhishekzambre/Documents/abhishekzambre.github.io/assets"))
print(disk_usage2("/Users/abhishekzambre/Documents/abhishekzambre.github.io/assets"))