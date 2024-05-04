# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 15:16:56 2024

@author: pauli
"""

import pandas as pd
from bs4 import BeautifulSoup as bs
import urllib.request

url="https://www.paruvendu.fr/a/voiture-occasion/voiture-7-places-et-plus/?p=2"


"""



"""

page=urllib.request.urlopen(url,timeout=35)
soup_url = bs(page, features="lxml")

# Fetch links as List of Tag Objects
links = soup_url.find_all("a", attrs={'class':'flex-1 overflow-hidden'})

# Store the links
links_list = []

# Loop for extracting links from Tag Objects
for link in links:
	links_list.append(link.get('href'))

donnees = []

links1=links_list[0:5]
links2=links_list[5:10]
links3=links_list[10:15]
links4=links_list[15:20]
links5=links_list[20:25]

for link in links5: 
    
    compteur=True
    
    url_voiture=link
    print(url_voiture)
    page=urllib.request.urlopen(url_voiture,timeout=10)
    soup = bs(page, features="lxml")
    
    categorie_elements = soup.find('h3',{'class':'autodetail-titre sepdetail14-ssbordure'})
    if categorie_elements:
        chaine =  categorie_elements.text.strip().replace('\n','')
        elements = chaine.split('\r')
        marque = elements[1]
        modele = elements[2]
    else :
        compteur=False
    
    categorie_version = soup.find('li',{'class':'vers fw-bold col-lg-6 col-12'})
    if categorie_version:
        version = categorie_version.text.strip().replace('\n', '')
    else:
        compteur=False

    categorie_prix = soup.find('li',{'class':'px fw-bold col-lg-6 col-12'})
    if categorie_prix:
        prix = categorie_prix.find("span",{'class':"fw-normal"})
        prix = prix.text.strip().replace('\n', '')
        print(prix)
    else:
        compteur=False
    
    categorie_annee = soup.find('li',{'class':'ann fw-bold col-lg-6 col-12'})
    if categorie_annee:
        annee=categorie_annee.find("span",{'class':"fw-normal"})
        for lien in annee.find_all(['div', 'br']):
            lien.extract()
        annee = annee.get_text(strip=True).replace('\n','')
    else:
        compteur=False

    categorie_km = soup.find('li',{'class':'kil fw-bold col-lg-6 col-12'})
    if categorie_km:
        km=categorie_km.find("span",{'class':"fw-normal"})
        km = km.text.strip().replace('\n', '')
    else:
        compteur=False

    categorie_energie = soup.find('li',{'class':'en fw-bold col-lg-6 col-12'})
    if categorie_energie:
        energie=categorie_energie.find("span",{'class':"fw-normal"})
        energie = energie.text.strip().replace('\n', '')
    else:
        compteur=False

    categorie_transmission = soup.find('li',{'class':'vit fw-bold col-lg-6 col-12'})
    if categorie_transmission:
        transmission=categorie_transmission.find("span",{'class':"fw-normal"})
        transmission = transmission.text.strip().replace('\n', '')
    else:
        compteur=False

    categorie_portes = soup.find('li',{'class':'carro fw-bold col-lg-6 col-12'})
    if categorie_portes:
        portes=categorie_portes.find("span",{'class':"fw-normal"})
        portes = portes.text.strip().replace('\n', '')
    else:
        compteur=False
        
    categorie_puissance = soup.find('li',{'class':'puiss fw-bold col-lg-6 col-12'})
    if categorie_puissance:
        puissance=categorie_puissance.find("span",{'class':"fw-normal"})
        puissance = puissance.text.strip().replace('\n', '')
    else:
        compteur=False
        
    categorie_place = soup.find('li',{'class':'por fw-bold col-lg-6 col-12'})
    if categorie_place:
        place=categorie_place.find("span",{'class':"fw-normal"})
        place = place.text.strip().replace('\n', '')
    else:
        compteur=False
    
    categorie_emission = soup.find('li',{'class':'emiss fw-bold col-lg-6 col-12'})
    if categorie_emission:
        emission = categorie_emission.find("span",{'class':"fw-normal"})
        emission = emission.text.strip().replace('\n', '')
    else:
        compteur=False
    
    categorie_consommation = soup.find('li',{'class':'cons fw-bold col-lg-6 col-12'})
    if categorie_consommation:
        consommation = categorie_consommation.find("span",{'class':"fw-normal"})
        consommation = consommation.text.strip().replace('\n', '')
    else:
        compteur=False
        
    categorie_description = soup.find('div',{'class':'im12_txt_ann im12_txt_ann_auto'})
    if categorie_description:
        description = categorie_description.find("div",{'class':"txt_annonceauto"})
        description = description.text.strip().replace('\n', '')
    else:
        compteur=False
        
    categorie_couleur = soup.find('li',{'class':'nologo'})
    if categorie_couleur:
        couleur = categorie_couleur.find("span")
        couleur = couleur.text.strip().replace('\n', '')
        #print(couleur)
    else:
        compteur=False
        
    if compteur ==True:

        donnees.append({
            "Marque":marque,
            "Modele":modele,
            "Prix ":prix,
            "Annee ":annee,
            "Kilometrage ":km,
            "Energie ":energie,
            "Transmission ":transmission,
            "Nombres de portes ":portes,
            "Puissance ":puissance,
            "Nombre de places":place,
            "Emission de CO2":emission,
            "Consommation de carburant":consommation,
            "Couleur":couleur,
            'Version ':version,
            "Description":description,
            "Url":url_voiture
            })
#pour afficher le tableau:
print(donnees)

#pour enregistrer en csv

df = pd.DataFrame(donnees)

df.to_csv('donnees_voiture_7places10.csv', index=False, sep='|', encoding='utf-8')


print(df.info())
print("Les données ont été enregistrées avec succès")






























