import requests 
from getpass import getpass
endpoint = 'http://127.0.0.1:8000/formation/auth'
username = input('entrer votre username:\n')
password = getpass('Entrer le mot de passe:\n ')
auth_response= requests.post(endpoint, json={'username':username, 'password':password})
print(auth_response.json())

endpoint = "http://localhost:8000/formation/Niveau/Champ/" #permet de rendre a httpbin.org
response = requests.get(endpoint) #params={'abc':124},  json={'query':'hi'}) # recupere les données , param permet d'envoyer les donnee par l'url post permet d'envoyer les données dans la bd
print(response.json())  
print(response.status_code)
