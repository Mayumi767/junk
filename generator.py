import requests
import re

repo = "Mayumi767/junk"
API_url = f'https://api.github.com/repos/{repo}/contents'


try:
	with requests.get(API_url) as response:
	   print(response.status_code)
	   imageUrls = [{'url': file['download_url']} for file in response.json() if file['type'] == 'file' and re.match(r'.*\.(png|jpe?g|gif)$', file['name'], re.IGNORECASE)]
	   print(imageUrls)
	   
except Exception as e:
	print("An error occurred:", e)


