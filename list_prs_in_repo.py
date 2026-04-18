import requests

def get_PR_authors(item):
        response=requests.get(item)
        if response.status_code == 200:
             data_dict=response.json() # parses JSON into Dict
             count_prs(data_dict)
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
    print(creators_data)

    
owner_name=input("Enter a GitHub owner name:")
repo_name=input("Enter a Repo name:")

pr_list=get_PR_authors(f"https://api.github.com/repos/{owner_name}/{repo_name}/pulls")

print(pr_list)