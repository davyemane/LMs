import requests 

endpoint = "http://localhost:8000/formation/Niveau/Champ/" #permet de rendre a httpbin.org
response = requests.get(endpoint) #params={'abc':124},  json={'query':'hi'}) # recupere les données , param permet d'envoyer les donnee par l'url post permet d'envoyer les données dans la bd
print(response.json('Niv'))  
print(response.status_code)
