import requests
from bs4 import BeautifulSoup
import re
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# Pola URL sosial media yang umum
SOCIAL_PATTERNS = {
    "Facebook": r"https?://(www\.)?facebook\.com/[^\s\"'>]+",
    "Twitter": r"https?://(www\.)?twitter\.com/[^\s\"'>]+",
    "Instagram": r"https?://(www\.)?instagram\.com/[^\s\"'>]+",
    "LinkedIn": r"https?://(www\.)?linkedin\.com/[^\s\"'>]+",
    "YouTube": r"https?://(www\.)?youtube\.com/[^\s\"'>]+",
    "TikTok": r"https?://(www\.)?tiktok\.com/@[^\s\"'>]+"
}

def extract_social_links(html):
    soup = BeautifulSoup(html, "html.parser")
    links = set(a['href'] for a in soup.find_all('a', href=True))
    social_links = {}

    for platform, pattern in SOCIAL_PATTERNS.items():
        matched = [link for link in links if re.match(pattern, link)]
        if matched:
            social_links[platform] = matched
    return social_links

def get_social_from_domain(domain):
    url = f"http://{domain}"
    print(f"[+] Mengakses situs: {url}")
    response = requests.get(url, verify=False)
    response.raise_for_status()

    return extract_social_links(response.text)

def target(domain):
    try:
        hasil = get_social_from_domain(domain)

        if hasil:
            print("\n[=] Ditemukan akun sosial media:")
            with open(f"{domain}_social.txt", 'w') as file:
                for platform, links in hasil.items():
                    for link in links:
                        print(f"{platform}: {link}")
                        file.write(f"{link}\n")
            input(f"Result saved on {domain}_social.txt")
        else:
            input("\n[-] Tidak ditemukan link sosial media pada halaman utama.")
    except requests.exceptions.ConnectionError:
        input("INVALID DOMAIN (PASTIKAN KONEKSI INTERNET ANDA STABIL DAN INPUT DENGAN BENAR)")
