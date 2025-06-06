import subprocess

def lookup(domain, record_type):
	result = subprocess.run(
		["nslookup", "-type="+record_type, domain],
		capture_output=True, text=True, check=True
	)
	return result.stdout

def nslookup(domain):
	try:
		result = ""
		for record_type in ['A', 'CNAME', 'MX', 'NS']:
   		 result += f"{record_type} record for {domain}:\n{lookup(domain, record_type)}\n"
		with open(f"{domain}_dns.txt", 'w') as file:
			file.write(result)
		input(f"Result saved on {domain}_dns.txt")
	except subprocess.CalledProcessError:
		input("Invalid domain")

