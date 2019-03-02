import webbrowser
import os

def email():
	try:
		print "Email Services:\n"
		print "	1. CyberSpy"

		print "\n	Third Party Websites:"
		print "	2. OSINT BOOKMARKLETS v0.3"
		print "	3. Lullar.com"

		print "	4. EmailFinder"

		print "	x. Back to menu"
		option2 = raw_input(">> ")
		if option2 == "1":
			link = os.path.abspath("files/email.html")
			webbrowser.open(link, new=2)
		elif option2 == "2":
			link = os.path.abspath("files/osintemail.html")
			webbrowser.open(link, new=2)
		elif option2 == "3":
			webbrowser.open("http://com.lullar.com/", new=2)
		elif option2 == "4":
			webbrowser.open("https://www.emailfinder.com/", new=2)
		else:
			banner()

	except KeyboardInterrupt:
		print "\nBye!"
		exit()
def username():
 print "Hi" 

def banner():
	print """
                .------.....______
               /                  '
              /                    \ 
             /'-----......_______--|
             |                     [
            /                       \ 
  _.-----''/''-----......._________--|__,...
 '..__                                    _/
      ''''--------___________--------'''''
            /                       |
           /                        |
          /                        /
         [__                       |
            /                      |
            \                |     |
            /               /      |
            |         __..-'       |
             ""'""''""             |
                  \     \          \__
                   |           __--"  /
                   |_____..--''MCDs  /
              \"'"'"        ___...__/
               \____...---''


"""
	menu()

def menu():

	print """CyberSpy - The Ultimate Doxing Web Toolkit
By Michael C. Dim

Services:

	1. Email Search
	2. Username Search
	3. Legal name Search
	4. Phone number Search
	5. IP Address Seach
	6. Reverse Image Search
	7. Image Data Extraction
	8. ZIP Code Search
	9. Make a report
	x. Exit CyberSpy
"""
	try:
		option = raw_input(">> ")
	except KeyboardInterrupt:
		print "\nBye!"
		exit()
	if option == "1":
		email()
	elif option == "2":
		username()
	else:
		exit()


	
banner()
