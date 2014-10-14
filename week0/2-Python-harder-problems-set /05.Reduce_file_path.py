#Rturning the reduced version of the path

def reduce_file_path(path):
	path = path.replace('//', 'd/')
	path = path.split('/')
	for index in range (0, len(path)):
		if "d" in path: 
			path.remove('d')
		if ".." in path: 
			i = path.index('..')
			path.remove('..')
			path = path[:i-2] + path[i:]
		if '.' in path:
			path.remove('.')		
	return '/' + "/".join(path)[:-1]


