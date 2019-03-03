import webbrowser
import os

def email():
	print "Email Services:\n"
	print "	1. CyberSpy"
	print "	2. OSINT BOOKMARKLETS v0.3"
	print "	Third Party Websites:"
	print "	3. com.lullar.com"
	print "	4. email-checker.net"
	print "	5. EmailFinder"
	print "\n	x. Back to menu\n"
	try:
		option2 = raw_input(">> ")
	except KeyboardInterrupt:
		print "\nBye!"
		exit()
	if option2 == "1":
		link = os.path.abspath("files/email.html")
		webbrowser.open(link, new=2)
	elif option2 == "2":
		link = os.path.abspath("files/osintemail.html")
		webbrowser.open(link, new=2)
	elif option2 == "3":
		webbrowser.open("http://com.lullar.com/", new=2)
	elif option2 == "4":
		webbrowser.open("https://email-checker.net/", new=2)
	elif option2 == "5":
		webbrowser.open("https://www.emailfinder.com/", new=2)
	else:
		banner()

def username():
	print "Username Services:\n"
	print "	1. CyberSpy"
	print "	2. OSINT BOOKMARKLETS v0.3"
	print "	Third Party Websites:"
	print "	3. com.lullar.com"
	print "	4. Google Advanced Search"
	print "	5. Pipl.com"
	print "	6. WebMii"
	print "	7. PeekYou"
	print "\n	x. Back to menu\n"
	try:
		option2 = raw_input(">> ")
	except KeyboardInterrupt:
		print "\nBye!"
		exit()
	if option2 == "1":
		link = os.path.abspath("files/username.html")
		webbrowser.open(link, new=2)
	elif option2 == "2":
		link = os.path.abspath("files/osintusername.html")
		webbrowser.open(link, new=2)
	elif option2 == "3":
		webbrowser.open("http://com.lullar.com/", new=2)
	elif option2 == "4":
		webbrowser.open("https://www.google.com/advanced_search", new=2)
	elif option2 == "5":
		webbrowser.open("http://www.pipl.com", new=2)
	elif option2 == "6":
		webbrowser.open("http://webmii.com/", new=2) #legal names too
	elif option2 == "7":
		webbrowser.open("https://www.peekyou.com/username", new=2) #legal names too
	else:
		banner()

def legalname():
	print "Legal Name Services:\n"
	print "	1. OSINT BOOKMARKLETS v0.3"
	print "	Third Party Websites:"
	print "	2. White Pages"
	print "	3. com.lullar.com"
	print "	4. ZabaSearch (US)"
	print "	5. Pipl.com"
	print "	6. WebMii"
	print "	7. PeekYou"
	print "	8. 411.com"	
	print "	9. Public Records"
	print "\n	x. Back to menu\n"
	try:
		option2 = raw_input(">> ")
	except KeyboardInterrupt:
		print "\nBye!"
		exit()
	if option2 == "1":
		webbrowser.open("", new=2)
	elif option2 == "2":
		webbrowser.open("https://whitepages.plus/", new=2)
	elif option2 == "3":
		webbrowser.open("http://com.lullar.com/", new=2)
	elif option2 == "4":
		webbrowser.open("https://www.google.com/advanced_search", new=2)
	elif option2 == "5":
		webbrowser.open("http://www.pipl.com", new=2)
	elif option2 == "6":
		webbrowser.open("http://webmii.com/", new=2)
	elif option2 == "7":
		webbrowser.open("https://www.peekyou.com/", new=2)
	elif option2 == "8":
		webbrowser.open("https://www.411.com/", new=2)
	elif option2 == "9":
		webbrowser.open("https://publicrecords.directory/", new=2)
	else:
		banner()

def number():
	print "Phone number Services:\n"
	print "	1. CyberSpy"
	print "	2. OSINT BOOKMARKLETS v0.3"	
	print "	Third Party Websites:"
	print "	3. PeekYou"
	print "	4. ZabaSearch"
	print "	5. WhoCalld"
	print "\n	x. Back to menu\n"
	try:
		option2 = raw_input(">> ")
	except KeyboardInterrupt:
		print "\nBye!"
		exit()
	if option2 == "1":
		link = os.path.abspath("files/phone.html")
		webbrowser.open(link, new=2)
	if option2 == "2":
		link = os.path.abspath("files/osintphone.html")
		webbrowser.open(link, new=2)		
	elif option2 == "3":
		webbrowser.open("https://www.peekyou.com/phone", new=2)
	elif option2 == "4":
		webbrowser.open("https://www.zabasearch.com/reverse-phone-lookup/", new=2)
	elif option2 == "5":
		webbrowser.open("https://whocalld.com", new=2)
	elif option2 == "6":
		webbrowser.open("", new=2)
	else:
		banner()
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
	5. IP Address services
	6. Image services
	7. ZIP Code Search
	8. Make a report
	9. Other Websites
	0. GeoLocation
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
	elif option == "3":
		legalname()
	elif option == "4":
		number()
	else:
		exit()


	
banner()
