import requests
import time

API_URL = 'https://api.telegram.org/bot'
with open(r"..\.venv\env") as file:
	BOT_TOKEN = file.readline()
TEXT = 'Ура! Классный апдейт!'

def update_cat():
    update = requests.get('https://api.thecatapi.com/v1/images/search').json()
    for res in update:
        return(res['url'])
    
foto_cat:str = update_cat()

offset = -2
chat_id: int

updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()


for result in updates['result']:
    offset = result['update_id']
    chat_id = result['message']['from']['id']
    requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')
    requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={foto_cat}')
