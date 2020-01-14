import requests
import MistSystems as Mist
import ngrok_wrapper as NGROK
import os
import time



time.sleep(5)
mist_apikey = os.environ['MIST_API']
mist_org = os.environ['MIST_ORG']
mist_site = os.environ['MIST_SITE']

ngrok_url = NGROK.Get_NGROK_Tunnel()
webhook = Mist.CreateWebhook(mist_site, ngrok_url, mist_apikey)
print(webhook.json)

