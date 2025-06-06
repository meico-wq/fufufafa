from pyfiglet import figlet_format
from colorama import Fore, init
import os, re
from modules import whois_scan, dns_scan, email_harvester, sosmed_scan
init(autoreset=True)

banner = figlet_format("FufuFafa", font="slant")

menu_items = [
	"1. Whois lookup",
	"2. DNS lookup",
	"3. Email harvester",
	"4. Social media scan",
	"5. Exit"
]
description = """
A lightweight OSINT tool for performing
WHOIS checks, DNS lookups, email harvesting,
and social media scanning.

Coded by ./meicookies
"""

print(Fore.CYAN + banner)
print(Fore.CYAN + description)

domain = input("Input domain:\n> ")
pattern = r"^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$"

if re.match(pattern, domain):
	while True:
		os.system("clear")
		print(Fore.WHITE + "Target: " + Fore.GREEN + domain)
		for item in menu_items:
	   	 print(Fore.YELLOW + item)
		pilih = input("> ")
		if pilih == "1":
			whois_scan.target(domain)
		elif pilih == "2":
			dns_scan.nslookup(domain)
		elif pilih == "3":
			email_harvester.target(domain)
		elif pilih == "4":
			sosmed_scan.target(domain)
		elif pilih == "5":
			break
		else:
			input(Fore.RED + "Invalid input " + pilih)
else:
	print(Fore.RED + "Invalid domain " + domain)
