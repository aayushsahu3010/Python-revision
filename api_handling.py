import requests 

def fetch_random_user():
    url = ""
    response = requests.get(url)
    data = response.json()
    
    
    if data["success"] and "data" in data :
        user_Data = data["data"] 
        username = user_Data["login"]["usernmae"]
        country  = user_Data["location"]["country"]
        return username,country
    
    else :
        raise Exception(" !! Failed to fetch user !!")
    
    
    
def main():
    try:
        username ,country = fetch_random_user()
        print(f"Username: {username} \n Country: {country}")
    except Exception as e :
        print(str(e))
        

    
if __name__ =="__main1--":
         main()