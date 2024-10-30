import requests
import csv
GITHUB_TOKEN = '<My API token'
headers = {'Authorization': f'token {GITHUB_TOKEN}'}

def get_repositories(username):
    url = f'https://api.github.com/users/{username}/repos?per_page=100&page='
    repositories = []
    
    page = 1
    while True:
        response = requests.get(url + str(page), headers=headers)
        response.raise_for_status()
        repos = response.json()
        
        if not repos:   
            break
        
        for repo in repos:
            repositories.append({
                'login': username,
                'full_name': repo.get('full_name', ''),
                'created_at': repo.get('created_at', ''),
                'stargazers_count': repo.get('stargazers_count', 0),
                'watchers_count': repo.get('watchers_count', 0),
                'language': repo.get('language', ''),
                'has_projects': repo.get('has_projects', False),
                'has_wiki': repo.get('has_wiki', False),
                'license_name': repo['license']['name'] if repo.get('license') else ''  
            })
        
        page += 1
        if len(repositories) >= 500:
            break
    
    return repositories[:500]

def main():

    users = []
    with open('users.csv', mode='r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            users.append(row['login'])   
    with open('repositories.csv', mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = [
            'login', 'full_name', 'created_at', 'stargazers_count', 
            'watchers_count', 'language', 'has_projects', 
            'has_wiki', 'license_name'
        ]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        for username in users:
            print(f'Fetching repositories for user: {username}')
            repos = get_repositories(username)
            for repo in repos:
                writer.writerow(repo)

if __name__ == '__main__':
    main()
