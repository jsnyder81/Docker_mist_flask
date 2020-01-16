#!/usr/bin/env python3
import sys
import time
import MistSystems as Mist
import ngrok_wrapper as NGROK
import os
import signal

def cleanup(signalNumber, frame):
    print("CAUGHT SIG-TERM")
    mist_apikey = os.environ['MIST_API']
    mist_site = os.environ['MIST_SITE']
    webhook_id = os.environ['MIST_WEBHOOK_ID']
    delete_response = Mist.DeleteWebhook(mist_site, webhook_id, mist_apikey)
    print(delete_response.json())
    sys.exit(0)


def main():
    time.sleep(10)
    mist_apikey = os.environ['MIST_API']
    mist_org = os.environ['MIST_ORG']
    mist_site = os.environ['MIST_SITE']
    ngrok_url = NGROK.Get_NGROK_Tunnel()
    webhook = Mist.CreateWebhook(mist_site, ngrok_url, mist_apikey)
    webhook_id = webhook.json()['id']
    os.environ['MIST_WEBHOOK_ID'] = webhook_id
    signal.signal(signal.SIGTERM, cleanup)
    x = True
    while x:
        print("waiting")
        time.sleep(5)


if __name__ == '__main__':
    main()