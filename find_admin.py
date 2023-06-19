#!/usr/bin/env python3
import os
import requests
from bs4 import BeautifulSoup

def find_admin(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        admin_tags = soup.find_all(class_="admin")
        admins = [tag.get_text() for tag in admin_tags]
        return admins
    except requests.exceptions.RequestException as e:
        print("Gabim gjatë kërkesës së faqes:", e)
        return []

def main():
    website_url = input("Shkruani URL-në e uebsajtit: ")
    admins = find_admin(website_url)
    if admins:
        print("Administratorët e gjetur:")
        for admin in admins:
            print(admin)
    else:
        print("Nuk u gjetën administratorë.")

if __name__ == '__main__':
    main()
