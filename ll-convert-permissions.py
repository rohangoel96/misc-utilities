'''

Reads the output of the ll command in bash (stored in data.txt), for example:
	-rwxrwxr-x  1 rohan rohan  5878 Feb 26 22:11 edit.pike*
	-rw-r--r--  1 root  root    532 Feb 26 22:13 export
Converts the permission to numeric format
And formats the string as required for example (stores it into output.txt):
	$(INSTALL) -m775 tools/edit.pike* $(DESTDIR)/$(STEAMDIR)/tools
	$(INSTALL) -m644 tools/export $(DESTDIR)/$(STEAMDIR)/tools

'''

in_file = open('data.txt', 'r')
out_file = open('output.txt', 'w')

def permissionStringToNumber(permissionString):
	formattedString = permissionString.replace('r','1').replace('w','1').replace('x','1').replace('-','0')
	firstDigit = int(formattedString[:3],2)
	secondDigit = int(formattedString[3:6],2)
	thirdDigit = int(formattedString[6:9],2)
	return str(firstDigit)+str(secondDigit)+str(thirdDigit)

def formatDataPrint(fileName,permission):
	if permission=='000':
		return "---------> "+fileName+" is a directory"
	else:	
		return "$(INSTALL) -m"+permission+" tools/"+fileName+" $(DESTDIR)/$(STEAMDIR)/tools"

for line in in_file:
	presentLine = line.split()
	if presentLine[0][0]=='-': #directories shown as 000 permission
		permissionString = presentLine[0][1:]
	else:
		permissionString = '00000000' 
	
	fileName = presentLine[8]
	permissionNumber = permissionStringToNumber(permissionString)

	print formatDataPrint(fileName,permissionNumber)
	out_file.write(formatDataPrint(fileName,permissionNumber)+"\n")

in_file.close()
out_file.close()