from whois import whois
import json
def target(domain):
   try:
      result = { "whois": whois(domain) }
      with open(f"{domain}_whois.json", 'w') as file:
         file.write(json.dumps(result, default=str))
      input(f"Result saved on {domain}_whois.json")
   except:
      input("INVALID DOMAIN")
