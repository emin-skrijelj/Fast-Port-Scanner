import requests 

url = "https://discordapp.com/api/webhooks/1048309652774998046/Hn3fX4pjkHOm0s8sH61i159YrsN0mh-QsbwhngavnenpT8JlfmbEI_J3UxlxNuHFT8_g" #webhook url, from here: https://i.imgur.com/f9XnAew.png

#for all params, see https://discordapp.com/developers/docs/resources/webhook#execute-webhook
data = {
    "content" : "message content",
    "username" : "Port Scanner"
}

#leave this out if you dont want an embed
#for all params, see https://discordapp.com/developers/docs/resources/channel#embed-object
# data["embeds"] = [
#     {
#         "description" : "text in embed",
#         "title" : "embed title"
#     }
# ]

result = requests.post(url, json = data)

try:
    result.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(err)
else:
    print("Payload delivered successfully, code {}.".format(result.status_code))

#result: https://i.imgur.com/DRqXQzA.png
