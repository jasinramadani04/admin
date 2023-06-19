import requests
from bs4 import BeautifulSoup

def detekto_administratorin(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        administrator = soup.find('meta', attrs={'name': 'author'})
        if administrator:
            return administrator['content']
        else:
            return "Nuk u gjet informacion rreth administratorit."
    except requests.exceptions.RequestException as e:
        return "Gabim gjatë lidhjes me faqen: " + str(e)

def detekto_autoret(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        autore = soup.find_all('meta', attrs={'name': 'author'})
        if autore:
            return [a['content'] for a in autore]
        else:
            return "Nuk u gjet informacion rreth autorëve."
    except requests.exceptions.RequestException as e:
        return "Gabim gjatë lidhjes me faqen: " + str(e)

# Përdorimi i skriptit
url_faqe = 'https://www.example.com'
administrator = detekto_administratorin(url_faqe)
print("Administratori i faqes është:", administrator)

autorët = detekto_autoret(url_faqe)
print("Autorët e faqes janë:", autorët)
