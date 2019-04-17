import requests
import json
import argparse
import shutil
import os
path = os.getcwd() + "/emojis/"
parser = argparse.ArgumentParser()
parser.add_argument("guild")
args = parser.parse_args()
token = 'tokenhere'
headers = {
    'authorization': '%s'%token
}
discordapi = "https://ptb.discordapp.com/api/v6/"
response = requests.get(discordapi + "guilds/%s/emojis"%args.guild, headers=headers)
j = json.loads(response.text)
i = 0
os.mkdir(path)
while(i < 51):
    id = j[i]['id']
    name = j[i]['name']
    response2 = requests.get("https://cdn.discordapp.com/emojis/%s.png"%id, stream=True)
    
    with open(path + '%s.png'%name, 'wb') as out_file:
        shutil.copyfileobj(response2.raw,out_file)
    i += 1
    

     
