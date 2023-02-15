import webbrowser
import urllib
import urllib.request

from googlesearch import search

from website_explorer import find_hyperlinks
from website_explorer import wikipedia_explorer

print('Type \'exit\' to quit from IVA')

while True:
	command_contains_goto_visit = 0
	query = input('\nEnter your command : ')
	
	if query == 'exit':
		break
	
	search_results = search(query, tld = 'co.in', num=10, stop=10, pause=2)
	

	#since search_results is a 'generator' datatype, we have to use an iterator to access it's elements.
	#So the below loop is for accessing the first element only
	website_url = ''
	
	
	for x in search_results:
		website_url = x
		break
		
		
	#to extract domain name from website url	
	website_domain = ''
	
	
	for x in range(len(website_url)):
		if website_url[x] == 'h' and website_url[x+1] == 't' and website_url[x+2] == 't' and website_url[x+3] == 'p':
			
			while True:
				if website_url[x] == '/':
					if website_url[x+1] == '/':
						break	
				x = x+1
			
			x = x+2
			
			while website_url[x] != '/':
				website_domain += website_url[x]
				x = x+1
			print('Domain name of the website is: ', website_domain)
			break
					
			
	
	website_name = website_url	
	
	print('Visting  '+website_url)
	
	weburl = urllib.request.urlopen(website_url) #for getting status codes, etc. Need to learn more about the two methods
	webbrowser.open_new_tab(website_url)  #to open the site in a new tab
       
			
	if weburl.getcode() == 200:
		print('Url successfully visited...')
		data = str(weburl.read())
		
		#to write the html contents to file named '[destination_name].txt'
		#web_file = open('explored_sites/'+website_name+'.txt', 'w')
		#web_file.write(str(data))
		#web_file.close()
		
		#for test purposes
		#sample_file = open('sample_website.txt', 'r')
		#sample_file.seek(0)
		#data = sample_file.read()
		
		links_dict = {}
		
		links_dict = find_hyperlinks(data)
				
		link_file = open('explored_sites/current_links.txt', 'w')
				
		count = 0
		for key in links_dict:
			count = count + 1
			link_file.write(str(count)+'. '+key+'  ->  '+links_dict[key]+'\n')
		
		print('\nWe found these hyperlinks in the website...\n ')
		count = 0
		for key in links_dict:
			count = count + 1
			print(str(count)+'. '+key+': '+links_dict[key]+'\n')
			
		#To goto one of the links
		while True:
			status = input('Do you want to goto a link by, if so how do you want to specify the link \na. Number\nb. Link name\nNOTE: Tell or enter \'z\' to skip\nYour Input: ')
			if status == 'z':
				break
				pass
		
			elif status == 'a':
				number = int(input('Enter or tell the link number: '))
			
				count = 1
				for key in links_dict:
					if count == number:
						print('Visiting ',key,'...\n')
						webbrowser.open_new_tab(links_dict[key])
						
						break
					count = count + 1
				break
		
			elif status == 'b':
				break
				pass
		
			else:
				print('Invalid input...\n')
		
				
		else:
			print('Url parsing unsuccessful..')

print('\nGoodbye sir...\n')
