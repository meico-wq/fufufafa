import requests
import re
from bs4 import BeautifulSoup
"""
di sini gw menggunakan crt.sh untuk mendapatkan subdomain
dari si target nah setelah mendapatkan semua subdomainnya
program akan melakukan scraping satu persatu dari subdomainnya
lalu mengekstrak email yg tertera (jika ada) menggunakan regex
tapi namanya juga tool lightweight jangan harap lu bisa dapetin
semua email dari si target karena gw cuman menggunakan crt.sh sebagai
alat yg membantu mencarinya tidak seperti tools email harvester lain
yg menggunakan berbagai search engine atau sosmed dll sebagai
alat bantu nya tapi ide yg gw gunakan di sini cukup efektif

jika lu punya ide lain bisa kontak gw di facebook
facebook.com/meicookiez
gw juga masih belajar

oh iya pastikan koneksi internet lu stabil dan input dengan
benar untuk menggunakan tool ini biar gada kesalahan
"""
def get_subdomains_from_crtsh(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        subdomains = set()
        for entry in data:
            name_value = entry.get("name_value", "")
            for sub in name_value.split('\n'):
                if domain in sub:
                    subdomains.add(sub.strip())
        return list(subdomains)
    except Exception as e:
        print(f"❌ Gagal ambil dari crt.sh: {e}")
        return []

def get_emails_from_site(url):
    try:
        if not url.startswith("http"):
            url = "http://" + url  # fallback to http
        response = requests.get(url, timeout=10)
        html = response.text
        emails = set(re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", html))
        return emails
    except Exception:
        return set()

def email_harvester_from_crtsh(domain):
    subdomains = get_subdomains_from_crtsh(domain)
    print(f"🌐 Ditemukan {len(subdomains)} subdomain")
    all_emails = set()
    for subdomain in subdomains:
        print(f"🔎 Mengakses: {subdomain}")
        emails = get_emails_from_site(subdomain)
        all_emails.update(emails)
    return all_emails

def target(domain):
    emails = email_harvester_from_crtsh(domain)
    if len(emails) != 0:
        print("\n📧 Email ditemukan:")
        with open(f"{domain}_emails.txt", 'w') as file:
            for email in sorted(emails):
                print(email)
                file.write(f"{email}\n")
        input(f"Result saved on {domain}_emails.txt")
    else:
        input(f"NOT FOUND OR INVALID DOMAIN (PASTIKAN KONEKSI INTERNET ANDA STABIL DAN INPUT DENGAN BENAR)")
