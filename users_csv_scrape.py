 import requests
 import csv
  #Not sharing API token is a good practice
 GITHUB_TOKEN = '<My API TOKEN>'
 headers = {'Authorization': f'token {GITHUB_TOKEN}'}

 def search_users(location, min_followers):
     url = f'https://api.github.com/search/users?q=location:{location}+followers:>{min_followers}'
     users = []
     page = 1
     while True:
         response = requests.get(url + f"&page={page}", headers=headers)
         response.raise_for_status()
         data = response.json()
        
         users.extend(data.get('items', []))
        
         if 'items' not in data or len(data['items']) == 0:
             break
        
         page += 1
    
     return users
