import re
import json
import urllib.request

repo = "Mayumi767/junk"  # repo address <username>/<repo name>
Folder = "images"  # image folder in git repo

if Folder != '':
    API_url = f'https://api.github.com/repos/{repo}/contents/{Folder}'
else:
    API_url = f'https://api.github.com/repos/{repo}/contents'

try:
    with urllib.request.urlopen(API_url) as response:
        #print(response.status)
        if response.status == 200:
            content = response.read().decode('utf-8')
            files = json.loads(content)
            imageUrls = [{'url': file['download_url']} for file in files if file['type'] == 'file' and re.match(r'.*\.(png|jpe?g|gif)$', file['name'], re.IGNORECASE)]
            data = json.dumps(imageUrls)
            with open("data.json", "w") as file:
                json.dump(imageUrls, file)
        else:
            print("Request failed with status:", response.status)
            
except Exception as e:
    print("An error occurred:", e)
