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
 def get_user_details(username):
     url = f'https://api.github.com/users/{username}'
     response = requests.get(url, headers=headers)
     response.raise_for_status()
     return response.json()

 def clean_company_name(company):
     if company:
         return company.strip().lstrip('@').upper()
     return ''

 def main():
     location = 'Toronto'
     min_followers = 100

     with open('users.csv', mode='w', newline='', encoding='utf-8') as csv_file:
         fieldnames = [
             'login', 'name', 'company', 'location', 'email', 
             'hireable', 'bio', 'public_repos', 'followers', 
             'following', 'created_at'
         ]
         writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

         writer.writeheader()
         users = search_users(location, min_followers)
         print(f"Found {len(users)} users in {location} with over {min_followers} followers.")

         for user in users:
             username = user['login']
             user_details = get_user_details(username)
             user_data = {
                 'login': user_details.get('login', ''),
                 'name': user_details.get('name', ''),
                 'company': clean_company_name(user_details.get('company', '')),
                 'location': user_details.get('location', ''),
                 'email': user_details.get('email', ''),
                 'hireable': user_details.get('hireable', ''),
                 'bio': user_details.get('bio', ''),
                 'public_repos': user_details.get('public_repos', 0),
                 'followers': user_details.get('followers', 0),
                 'following': user_details.get('following', 0),
                 'created_at': user_details.get('created_at', '')
             }
            
             writer.writerow(user_data)

 if __name__ == '__main__':
     main()
