class CSVParser: 

	def __init__(self, path, headers = True):
		self.path = path
		self.headers = headers

		
		if headers:
			file = open(path, 'r')
			read = (file.read())
			
		else:
			file = open(path, 'r') 
			read = (file.read())
			newList = read.split('\n')
			headersList = range(0, len(newList))
			read = str(headersList) + read + '\n'
		self.read = read
	
	def get_row(self, row_index):
		list = []
		for i in range(0, len(self.read)):
			if (self.read[i] == '\n')
				list.append(i)
		row = []
		for x in list:
			if (row_index == x):
				row.append(read.read[x:x+1]

	def get_column(self, column):
		if (column == int):
			list = []
			readSplit = self.read.split('\n')
			for i in range(0, len(readSplit-1)):
				list.append((readSplit[i])[column])
				
		else:
			list = []
			readSplit = self.read.split('\n')
			for j in range(0, len(readSplit[0])):
				if (readSplit[j]==column):
					for k in range(0, len(readSplit-1)):
						list.append((readSplit[k])[j])
		return list			
		
	def transform_column(f, column, new_column_name=None):		
		newList = []
		for colu in self.read:
			if (colu == column):
				newList.append(colu)
		function = map(f, newList)
		return function