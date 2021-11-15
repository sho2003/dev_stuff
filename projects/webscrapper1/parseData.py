import json

with open('twitterData.json') as json_data:
    jsonData = json.load(json_data)

oCount = 0
for i in jsonData:
    if("obama" in i['tweet'].lower()):
        oCount += 1
        print(i['tweet'])
print("Obama was mentioned " + str(oCount) + " times")
