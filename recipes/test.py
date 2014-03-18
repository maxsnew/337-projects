import download

def main():
	pie = download.download_recipe("http://allrecipes.com/Recipe/Burrito-Pie")
	print pie
	return 
	
if __name__ == '__main__':
	main()