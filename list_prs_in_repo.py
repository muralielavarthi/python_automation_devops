# We will fetch list of Open Pull Requests

import requests
import os

def get_PR_authors(URL):
        response=requests.get(URL,headers=headers)
        if response.status_code == 200:
             data_dict=response.json() # parses JSON into Dict
             return count_prs(data_dict)
        else:
            print(f"unable to fetch data",response.status_code)

def count_prs(data):
    creators_data={}
    for line in data:
        creator=line["user"]["login"]
        if creator in creators_data:
            creators_data[creator]+=1
        else:
            creators_data[creator]=1
    return creators_data

    
owner_name=input("Enter a GitHub owner name:")
repo_name=input("Enter a Repo name:")

token=os.getenv("GIT_HUB_TOKEN")

# Github Account Authorization for Private Repos
headers = {
     "Authorization": f"Bearer {token}"
}

final_result=get_PR_authors(f"https://api.github.com/repos/{owner_name}/{repo_name}/pulls?state=open")
print(final_result)

#By default, GitHub API returns only 30 pull requests per page.
#If you want all PRs, please handle pagination
