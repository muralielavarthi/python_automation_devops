import requests

def get_PR_authors(item):
    try: 
        response=requests.get(item)
        if response.status_code == 200:
             data_dict=response.json() # parses JSON into Dict
             return data_dict
    except ConnectionError as conn_err: 
        return conn_err

owner_name=input("Enter a GitHub owner name:")
repo_name=input("Enter a Repo name:")

pr_list=get_PR_authors(f"https://api.github.com/repos/{owner_name}/{repo_name}/pulls")

print(pr_list[0]["user"]["login"])