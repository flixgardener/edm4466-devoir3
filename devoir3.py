# coding : utf-8
import requests, csv, json
from bs4 import BeautifulSoup

fichier = "articlesmariage.csv"



# Mon objectif est de créer un fichier csv avec tous les articles de mariage disponibles à l'achat en ligne
# sur le site de Dollarama..

entete = {
	"User-Agent":"Félix Desjardins",
	"From":"felixdesjardins1@gmail.com"
}

for x in range(1,9):
	url = "https://www.dollarama.com/fr-CA/activite/evenements-fetes-et-organisation-de-mariages?page="+str(x)
	contenu = requests.get(url,headers=entete)
	# print(contenu)
	page = BeautifulSoup(contenu.text, "html.parser")
	print()
	articles = page.find_all("div", class_="product-tile-text")
	
	for article in articles:
		print ((article.find("a", class_="js-display-name")).text)
		print ("_"*50)
		print ((article.find("div", class_="product-tile-price")).text)
	
	dead = open(fichier,"a")
	obies = csv.writer(dead)
	obies.writerow(articles)

	
