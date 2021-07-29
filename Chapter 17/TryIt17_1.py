import requests

'''Make an API call and store the response'''
urlhaskell = 'https://api.github.com/search/repositories?q=language:haskell&sort=stars'
url_javascript = 'https://api.github.com/search/repositories?q=language:javascript&sort=stars'
url_ruby = 'https://api.github.com/search/repositories?q=language:ruby&sort=stars'
url_c = 'https://api.github.com/search/repositories?q=language:c&sort=stars'
url_java = 'https://api.github.com/search/repositories?q=language:java&sort=stars'
url_go = 'https://api.github.com/search/repositories?q=language:go&sort=stars'

headers = {'Accept': 'application/vnd.github.v3+json'}
r_javascript = requests.get(url_javascript, headers=headers)
rhaskell = requests.get(urlhaskell, headers = headers)
r_ruby = requests.get(url_ruby, headers=headers)
r_c = requests.get(url_c, headers=headers)
r_java = requests.get(url_java, headers=headers)
r_go = requests.get(url_go, headers=headers)

print(f"Status code heskell: {rhaskell.status_code}")
print(f"Status code javascript: {r_javascript.status_code}")
print(f"Status code ruby: {r_ruby.status_code}")
print(f"Status code c: {r_c.status_code}")
print(f"Status code java: {r_java.status_code}")
print(f"Status code go: {r_go.status_code}")

'''Store API response in variable'''
response_dict_haskell = rhaskell.json()
response_dict_javascript = r_javascript.json()
response_dict_java = r_java.json()
response_dict_c = r_c.json()
response_dict_ruby = r_ruby.json()
response_dict_go= r_go.json()
print(f"Total heskell repositories: {response_dict_haskell['total_count']}")
print(f"Total javascript repositories: {response_dict_javascript['total_count']}")
print(f"Total java repositories: {response_dict_java['total_count']}")
print(f"Total c repositories: {response_dict_c['total_count']}")
print(f"Total ruby repositories: {response_dict_ruby['total_count']}")
print(f"Total go repositories: {response_dict_go['total_count']}")


'''Explore information about the repositories'''
repo_dicts_haskell = response_dict_haskell['items']
repo_dicts_javascript = response_dict_javascript['items']
repo_dicts_java = response_dict_java['items']
repo_dicts_ruby = response_dict_ruby['items']
repo_dicts_c = response_dict_c['items']
repo_dicts_go = response_dict_go['items']
print(f" Javascript repositories returned : {len(repo_dicts_javascript)}")
print(f"Repositories haskell returned : {len(repo_dicts_haskell)}")
print(f" Java repositories returned : {len(repo_dicts_java)}")
print(f" Ruby repositories returned : {len(repo_dicts_ruby)}")
print(f" C repositories returned : {len(repo_dicts_c)}")
print(f" Go repositories returned : {len(repo_dicts_go)}")



'''Examine the first repository'''
print("\nSelected information about each repository:")
for repo_dict in repo_dicts_haskell:
    print("\nSelected information about haskell repository: ")
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")

for repo_dict in repo_dicts_javascript:
    print("\nSelected information about javascript repository: ")
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")

for repo_dict in repo_dicts_java:
    print("\nSelected information about java repository: ")
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")
for repo_dict in repo_dicts_ruby:
    print("\nSelected information about ruby repository: ")
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")
for repo_dict in repo_dicts_c:
    print("\nSelected information about c repository: ")
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")
for repo_dict in repo_dicts_go:
    print("\nSelected information about go repository: ")
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")
