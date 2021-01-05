import requests
from bs4 import BeautifulSoup

"""
    De nombreux sites ont des protection contre le scraping, le headers va donc nous permettre
    de contourner ce problème en usurpant les en-têtes que nous envoyons avec nos demandes pour
    ressembler à un navigateur légitime
"""
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

with open("C:\\Users\\munau\\OneDrive\\Bureau\\Projet MEcab\\url.txt", "r", encoding="utf-8") as f:
        # line est un tuple des url
        line = "https://ja.wikipedia.org/wiki/%E3%83%8D%E3%82%B3", "https://ja.wikipedia.org/wiki/%E5%AD%A6%E6%A0%A1", "https://ja.wikipedia.org/wiki/%E3%82%A2%E3%83%8B%E3%83%A1", "https://ja.wikipedia.org/wiki/%E5%AF%BF%E5%8F%B8", "https://ja.wikipedia.org/wiki/%E6%B5%B7", "https://ja.wikipedia.org/wiki/%E9%9D%92%E7%A9%BA", "https://ja.wikipedia.org/wiki/%E5%90%8D%E5%8F%A4%E5%B1%8B", "https://ja.wikipedia.org/wiki/%E9%9F%B3%E6%A5%BD", "https://ja.wikipedia.org/wiki/%E6%BC%AB%E7%94%BB"
        i = 0

        # On parcourt les url pour faire le scraping de chaque page et stocker le texte de la page dans des fichiers txt différents
        while i != len(line)-1:
            url = line[i]
            req = requests.get(url, headers)
            soup = BeautifulSoup(req.content, 'html.parser')
            with open("texte"+str(i)+".txt", "w", encoding="utf-8") as f2:
                f2.write(soup.get_text())
            i+=1


