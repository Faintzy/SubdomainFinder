import requests as req
import sys
import time

try:
	
	if sys.argv[1] == "help":

		print("basic: python3 sbfinder.py \n" +
			  "default wordlists: -wordlists")

except:

	pass

addr = input("[?] Site address (https://google.com): ")

if ("http" not in addr) or ("https" not in addr):
	
	addr = "http://|" + addr 

try:

	print("[!] Checking domain..")

	req.get(addr.replace("|", ""))

	print("[!] Working!")

except:

	print("Invalid Web Address")

	sys.exit()

userList = input("[?] path/to/wordlist.txt or default: ")

if len(userList) == 0:

	print("Wordlist not found")

	sys.exit()

try:

	if userList == "default":

		userList = "wordlists/wordlist.txt"

	wordlist = open(userList, "r").read()

	array = wordlist.split("\n")

	i = 0

	lives = []

	print("\n [OK] STARTED \n")

	while i < len(array):

		subdomain = array[i]

		replaced = addr.replace("|", subdomain + ".")

		try:

			req.get(replaced)

			lives.append(replaced)

			print("[OK] " + replaced)

		except:
			
			print("[!] " + replaced)

		if i == len(array) - 1:

			print("\n[END] Finished \n")

			if len(lives) > 0:

				for x in lives:

					print("    " + x)

			else: 

				sys.exit()

			print("\n[END] Finished \n")

		i += 1

except: 

	print("Wordlist not found")
