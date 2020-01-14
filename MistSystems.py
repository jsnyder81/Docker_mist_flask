import requests
import json

base_url = "api.mist.com"

class bandTemplate(object):
    band = ""
    disabled = ""
    channels = ""
    bandwidth = ""
    power_dbm = ""
    def __init__(self, myBand, myBandwidth, myChannels, myPowerdbm, bandDisabled):
        self.band = myBand
        self.bandwidth = myBandwidth
        self.channels = myChannels
        self.power_dbm = myPowerdbm
        self.disabld = bandDisabled

def CheckIfLoggedIn(session):
     #print("Checking if logged in via token")
     api_call = "/api/v1/self"
     request_url = "https://" + base_url + api_call
     header = {"content-type": "application/json"}
     response = session.get(request_url, headers=header, verify=False)
     r_json = response.json()
     if response.status_code == 200:
         return True
     else:
         return False

def CheckIfLoggedInToken(token_id):
   api_call = "/api/v1/self"
    req_url = "https://" + base_url + api_call
    header = {"content-type": "application/json", 'Authorization': 'token {}'.format(token_id)}
    session = requests.Session()
    response = session.get(req_url, headers=header, verify=False)
    r_json = response.json()
    if response.status_code == 200:
        return True
    else:
        return False

def LogInCredentials(session, email, password):
    LogInCredentials_url = "/api/v1/login"
    req_url = "https://" + base_url + LogInCredentials_url
    payload = {"email": email, "password": password}
    header = {"content-type": "application/json"}
    response = session.post(req_url, data=json.dumps(payload), headers=header, verify=False)
    r_json = response.json()
    csrftoken = session.cookies['csrftoken']

def GetAPIToken(session, email, password):
    #print("Getting API Token")
    token_url = "/api/v1/self/apitokens"
    req_url = "https://" + base_url + token_url
    session.get(req_url)
    csrftoken = session.cookies['csrftoken']
    login_data = dict(username=email, password=password, csrfmiddlewaretoken=csrftoken, next='/')
    response = session.post(req_url, data=login_data, headers=dict(Referer=req_url))
    r_json = response.json()
    print(str(r_json["key"]))
    auth_key = str(r_json["key"])
    return auth_key

def GetOrgs(auth_token):
    session = requests.Session()
    self_url = "/api/v1/self"
    response = Get(self_url, auth_token)
    myOrgs = []
    if response.status_code == 200:
        for org in response.json()['privileges']:
            if org['scope'] == 'org':
                myOrgs.append(str(org['org_id']))
    else:
        print("Error, status code" + str(response.status_code))
    return myOrgs

def CreateRFTemplate(org_id, template_name, country_code, template_24, template_5):
    payload = {
    "name":template_name,
    "country_code":country_code,
    "band_24":{
    "disabled":template_24.disabled,
    "channels":template_24.channels,
    "bandwidth":template_24.bandwidth,
    "power":template_24.power_dbm},
    "band_5":{
    "disabled":template_5.disabled,
    "channels":template_5.channels,
    "bandwidth":template_5.bandwidth,
    "power":template_5.power_dbm},
    }
    rf_template_url = "/api/v1/orgs/" + org_id + "/rftemplates"
    req_url = base_url + rf_template_url

    return template_ID

def GetSites(org_id, auth_token):
    site_url = "/api/v1/orgs/" + org_id + "/sites"
    response = Get(site_url, auth_token)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error: " + response.status_code)
        print("Message: " + response.json())

def GetDevices(site_id, auth_token):
    site_url = "/api/v1/sites/" + site_id + "/devices"
    response = Get(site_url, auth_token)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error: " + response.status_code)
        print("Message: " + response.json())

def GetDeviceStats(site_id, auth_token):
    site_url = "/api/v1/sites/" + site_id + "/stats/devices"
    response = Get(site_url, auth_token)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error: " + response.status_code)
        print("Message: " + response.json())

def GetClientsStats(site_id, auth_token):
    site_url = '/api/v1/sites/' + site_id + "/stats/clients"
    response = Get(site_url, auth_token)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error: " + response.status_code)
        print("Message: " + response.json())

def GetWXTags(site_id, auth_token):
    site_url = '/api/v1/sites/' + site_id + "/wxtags"
    response = Get(site_url, auth_token)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error: " + response.status_code)
        print("Message: " + response.json())

def GetWlans(org_id, site_id, auth_token):
    wlan_info = []
    try:
        for org_wlan in GetWlansbyOrg(org_id, auth_token):
                wlan_info.append(org_wlan)
    except:
        pass
    try:
        print("testing sites")
        for site_wlan in GetWlansbySite(site_id, auth_token):
            print("site found")
            wlan_info.append(site_wlan)
    except:
        print("exception")
        pass
    return wlan_info


def GetWlansbyOrg(org_id, auth_token):
    site_url = '/api/v1/orgs/' + org_id + "/wlans"
    response = Get(site_url, auth_token)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error: " + response.status_code)
        print("Message: " + response.json())

def GetWlansbySite(site_id, auth_token):
    site_url = '/api/v1/sites/' + site_id + "/wlans"
    response = Get(site_id, auth_token)
    print(response.json())
    if response.status_code == 200:
        return response.json()
    else:
        print("Error: " + response.status_code)
        print("Message: " + response.json())

def Post(url_extention, payload, auth_token):
    session = requests.Session()
    req_url = "https://" + base_url + url_extention
    header = {"content-type": "application/json", 'Authorization': 'token {}'.format(auth_token)}
    response = session.post(req_url, headers=header, data=json.dumps(payload), verify=False)
    return response

def Get(url_extention, auth_token):
    session = requests.Session()
    req_url = "https://" + base_url + url_extention
    header = {"content-type": "application/json", 'Authorization': 'token {}'.format(auth_token)}
    response = session.get(req_url, headers=header, verify=False)
    return response

def CreateWlanFromTemplate(site_id, Template, auth_token):
    wlan_url = "/api/v1/sites/" + site_id + "/wlans/"
    header = {"content-type": "application/json", 'Authorization': 'token {}'.format(auth_token)}
    response = Post(wlan_url, Template, auth_token)
    wlan_id = ""
    if response.status_code == 200:
        wlan_id = response.json()['id']
    else:
        print("Error: " + respons.status_code)
        print("Message: " + response.json())
    return wlan_id

def APStatsToInflux(apStats):
    output_json = []
    for device in apStats:
        json_body = {}
        json_body["measurement"] = "apStats"
        json_body["tags"] = {}
        json_body["fields"] = {}
        json_body["tags"]["name"] = device["name"]
        json_body["tags"]["mac"] = device["mac"]
        json_body["tags"]["serial"] = device["serial"]
        json_body["tags"]["site_id"] = device["site_id"]
        json_body["tags"]["status"] = device["status"]
        json_body["tags"]["model"] = device["model"]
        try:
            json_body["tags"]["version"] = device["version"]
        except:
            pass
        try:
            json_body["tags"]["ip"] = device["ip_stat"]["ip"]
            json_body["tags"]["netmask"] = device["ip_stat"]["netmask"]
            json_body["tags"]["gateway"] = device["ip_stat"]["gateway"]
            json_body["tags"]["band_24_channel"] = device["radio_stat"]["band_24"]["channel"]
            json_body["tags"]["band_5_channel"] = device["radio_stat"]["band_5"]["channel"]
        except:
            pass
        #AP Specific Stats
        try:
            json_body["fields"]["last_seen"] = device["last_seen"]
        except:
            pass
        if device['status'] == 'connected':
            json_body["fields"]["connected"] = 1
            json_body["fields"]["num_clients"] = device["num_clients"]
            # 2.4 GHZ stats
            json_body["fields"]["band_24_bandwidth"] = device["radio_stat"]["band_24"]["bandwidth"]
            json_body["fields"]["band_24_channel"] = device["radio_stat"]["band_24"]["channel"]
            json_body["fields"]["band_24_power"] = device["radio_stat"]["band_24"]["power"]
            json_body["fields"]["band_24_noise_floor"] = device["radio_stat"]["band_24"]["noise_floor"]
            json_body["fields"]["band_24_clients"] = device["radio_stat"]["band_24"]["num_clients"]
            json_body["fields"]["band_24_rx_bytes"] = device["radio_stat"]["band_24"]["rx_bytes"]
            json_body["fields"]["band_24_rx_pkts"] = device["radio_stat"]["band_24"]["rx_pkts"]
            json_body["fields"]["band_24_tx_bytes"] = device["radio_stat"]["band_24"]["tx_bytes"]
            json_body["fields"]["band_24_tx_pkts"] = device["radio_stat"]["band_24"]["tx_pkts"]
            json_body["fields"]["band_24_util_all"] = device["radio_stat"]["band_24"]["util_all"]
            json_body["fields"]["band_24_util_non_wifi"] = device["radio_stat"]["band_24"]["util_non_wifi"]
            json_body["fields"]["band_24_util_rx_in_bss"] = device["radio_stat"]["band_24"]["util_rx_in_bss"]
            json_body["fields"]["band_24_util_tx"] = device["radio_stat"]["band_24"]["util_tx"]
            json_body["fields"]["band_24_util_tx_unknown_wifi"] = device["radio_stat"]["band_24"]["util_unknown_wifi"]
            # 5GHz Stats
            json_body["fields"]["band_5_bandwidth"] = device["radio_stat"]["band_5"]["bandwidth"]
            json_body["fields"]["band_5_channel"] = device["radio_stat"]["band_5"]["channel"]
            json_body["fields"]["band_5_power"] = device["radio_stat"]["band_5"]["power"]
            json_body["fields"]["band_5_noise_floor"] = device["radio_stat"]["band_5"]["noise_floor"]
            json_body["fields"]["band_5_clients"] = device["radio_stat"]["band_5"]["num_clients"]
            json_body["fields"]["band_5_rx_bytes"] = device["radio_stat"]["band_5"]["rx_bytes"]
            json_body["fields"]["band_5_rx_pkts"] = device["radio_stat"]["band_5"]["rx_pkts"]
            json_body["fields"]["band_5_tx_bytes"] = device["radio_stat"]["band_5"]["tx_bytes"]
            json_body["fields"]["band_5_tx_pkts"] = device["radio_stat"]["band_5"]["tx_pkts"]
            json_body["fields"]["band_5_util_all"] = device["radio_stat"]["band_5"]["util_all"]
            json_body["fields"]["band_5_util_non_wifi"] = device["radio_stat"]["band_5"]["util_non_wifi"]
            json_body["fields"]["band_5_util_rx_in_bss"] = device["radio_stat"]["band_5"]["util_rx_in_bss"]
            json_body["fields"]["band_5_util_tx"] = device["radio_stat"]["band_5"]["util_tx"]
            json_body["fields"]["band_5_util_tx_unknown_wifi"] = device["radio_stat"]["band_5"]["util_unknown_wifi"]
            json_body["fields"]["rx_bps"] = device["rx_bps"]
            json_body["fields"]["rx_bytes"] = device["rx_bytes"]
            json_body["fields"]["rx_pkts"] = device["rx_pkts"]
            json_body["fields"]["tx_bps"] = device["rx_bps"]
            json_body["fields"]["tx_bytes"] = device["rx_bytes"]
            json_body["fields"]["tx_pkts"] = device["rx_pkts"]
            json_body["fields"]["uptime"] = device["uptime"]

        else:
            json_body["fields"]["connected"] = 0

        output_json.append(json_body)
    return output_json

def ClientStatsToInflux(ClientStats):
    output_json = []
    for client in ClientStats:
        json_body = {}
        json_body["measurement"] = "client_stats"
        json_body["tags"] = {}
        json_body["fields"] = {}
        try:
            json_body["tags"]["hostname"] = client["hostname"]
        except:
            json_body['tags']['hostname'] = client['mac']
        json_body["tags"]["mac"] = client["mac"]
        try:
            json_body["tags"]["ip"] = client["ip"]
        except:
            pass
        json_body["tags"]["site_id"] = client["site_id"]
        json_body["tags"]["manufacture"] = client["manufacture"]
        json_body["tags"]["proto"] = client["proto"]
        json_body["tags"]["ssid"] = client["ssid"]
        json_body["tags"]["dual_band"] = client["dual_band"]
        json_body["tags"]["key_mgmt"] = client["key_mgmt"]
        json_body["tags"]["band"] = client["band"]
        json_body["tags"]["username"] = client["username"]
        json_body["tags"]["vlan_id"] = client["vlan_id"]
        json_body["tags"]["channel"] = client["channel"]
        json_body["tags"]["bssid"] = client["bssid"]
        json_body["tags"]["ap_mac"] = client["ap_mac"]
        json_body["tags"]["ap_id"] = client["ap_id"]
        #json_body["tags"]["snr"] = client["snr"]
        #json_body["tags"]["rssi"] = client["rssi"]
        json_body["tags"]["ap_name"] = client["ap_name"]
        try:
            json_body["tags"]["wlan_name"] = client["wlan_name"]
        except:
            print("Client = " + client['mac'])
            print("WLAN_ID = " + client['wlan_id'])
            pass
        try:
            json_body["tags"]["tag"] = client["tag"]
        except:
            pass
        #client Specific Stats
        json_body["fields"]["rx_bps"] = client["rx_bps"]
        json_body["fields"]["rx_bytes"] = client["rx_bytes"]
        json_body["fields"]["rx_pkts"] = client["rx_pkts"]
        json_body["fields"]["rx_rate"] = client["rx_rate"]
        json_body["fields"]["rx_retries"] = client["rx_retries"]
        json_body["fields"]["tx_bps"] = client["tx_bps"]
        json_body["fields"]["tx_bytes"] = client["tx_bytes"]
        json_body["fields"]["tx_pkts"] = client["tx_pkts"]
        json_body["fields"]["tx_rate"] = client["tx_rate"]
        json_body["fields"]["tx_retries"] = client["tx_retries"]
        json_body["fields"]["uptime"] = client["uptime"]
        json_body["fields"]["rssi"] = client["rssi"]
        json_body["fields"]["snr"] = client["snr"]
        json_body["fields"]["band"] = client["band"]
        json_body["fields"]["channel"] = client["channel"]
        json_body['fields']['count'] = 1
        output_json.append(json_body)
    return output_json

def CreateWebhook(site_id, webhook_url, auth_token):
    api_url = "/api/v1/sites/" + site_id + "/webhooks"
    request_url = "https://" + base_url + api_url
    print(request_url)
    header = {"content-type": "application/json", 'Authorization': 'token {}'.format(auth_token)}
    payload = {
    "name": "analytic",
    "type": "http-post",
    "url": webhook_url,
    "secret": "secret",
    "verify_cert": False,
    "enabled": True,
    "topics": [ "location", "zone", "vbeacon", "rssizone", "asset-raw", "device-events", "alarms", "audits", "client-sessions", "device-updowns" ]}
    response = mist_Post(api_url, payload, auth_token)
    if response.status_code == 200:
        pass
    else:
        print("Error: " + str(response.status_code))
        print("Message: " + str(response))
        print(request_url)
    return response

def mist_Post(mist_url_extention, payload, mist_auth_token):
    mist_session = requests.Session()
    mist_req_url = "https://" + base_url + mist_url_extention
    header = {"content-type": "application/json", 'Authorization': 'token {}'.format(mist_auth_token)}
    response = mist_session.post(mist_req_url, headers=header, data=json.dumps(payload), verify=False)
    return response



