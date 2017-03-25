# A module for saving html web pages
def save_file(content, filename):
	with open(filename, 'wb') as f:
		f.write(content)
	print("Saved file")