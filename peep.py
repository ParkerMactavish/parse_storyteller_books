import argparse
from selenium import webdriver
import time

"""
#function name : arg_parse
#description : to define action of argument parsing
"""
def parse_arg():
	parser = argparse.ArgumentParser(description = 'Execute web parsing, edit the list of target parse, or output the result')
	parser.add_argument('cmd', help = 'Direct command', type = str, \
	nargs = '?')
	parser.add_argument('-author', dest = 'destAuthor', type = str, help = 'Change\
	 current editing author of the list', nargs = '*')
	parser.add_argument('-add_author', dest = 'addedAuthor', type = str, help =\
	'Add new author list', nargs = '*')
	parser.add_argument('-add_book', dest = 'addedBook', type = str, help = \
	'Add new book to the author list', nargs = '*')
	parser.add_argument('-plot', dest = 'plotOption', type = str, help = \
	'Plot the chosen range of reserved book,\
		all for all books of all authors,\
		author name for all books of the specific author,\
		book name for the specific book', nargs = '*')
	
	args = parser.parse_args()
	return args
	
def parse_web():
	driver = webdriver.Chrome(executable_path = "D:\Leisure Time\Storyteller_Stalker\driver\chromedriver.exe")
	time.sleep(3)
	driver.get('http://163.26.71.106/webpac/content.cfm?mid=3765&m=ss&k0=%E5%90%B8%E7%9D%9B%E7%9A%84%E7%A7%91%E5%AD%B8&t0=k&c0=and&si=&content&list_num=10&current_page=1&mt=&at=&sj=&py=&pr=&it=&lr=&lg=&si=1&contentlistcurrent_page=1&contentlist_num=10&lc=0&ye=&vo=&item_status_v=')
	return driver.page_source
	
if __name__ == '__main__':
	arg = parse_arg()
	if arg.destAuthor!=None and arg.addedAuthor==None and arg.plotOption==None:
		if arg.addedBook!=None:
			print(arg.destAuthor, arg.addedBook)
	print(parse_web())
		
	print(arg)