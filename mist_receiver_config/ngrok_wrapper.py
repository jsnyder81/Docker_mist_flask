import requests


def Get_NGROK_Tunnel(ip='ngrok', port=4040):
    header = {"content-type": "application/json"}
    response = requests.request("GET", 'http://ngrok:4040/api/tunnels', headers=header, data='')
    #response = requests.request("GET", 'http://localhost:4040/api/tunnels', headers=header, data='')
    return response.json()['tunnels'][0]['public_url']
