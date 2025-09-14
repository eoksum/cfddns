import json
import requests
import time

# DNS params
dnsName = "ddns.yourdomain.com"
dnsTtl = 1 # TTL 1 = Auto in CloudFlare
proxy = False # Enable proxying in CloudFlare

# CloudFlare API creds
authEmail = "youremail@domain.com"
authKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" # Obtain via My Profile >> API Tokens >> Global API Key
CfZoneId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" # Obtain via either API or DevTools >> Network
CfDnsRecordId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" # Obtain via either API or DevTools >> Network

# Set params for CloudFlare API request
headers = {
    "User-Agent": "CF DDNS Client",
    "X-Auth-Key": authKey,
    "Authorization": "Bearer " + authKey,
    "X-Auth-Email": authEmail,
    "Content-Type": "application/json"
}

data = {
	"name": dnsName,
    "ttl": dnsTtl,
    "type": "A",
    "comment": "CF DDNS Last Update: " + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()),
    "content": None,
    "proxied": proxy
}

# Retrieving WAN IP - ip-api.com
try:
    h = requests.get("http://ip-api.com/json/?fields=status,query", timeout=5)
    if h.status_code == 200:
        res = h.json()
        if res["status"] == "success":
            data["content"] = res["query"]
except:
    pass

# Retrieving WAN IP - wtfismyip.com (if previous one fails)
if data["content"] is None:
    try:
        h = requests.get("https://wtfismyip.com/text", timeout=5)
        if h.status_code == 200:
            data["content"] = h.text
    except:
        pass

if data["content"] is None:
    print("Failed to retrieve WAN IP! Quitting...")
    exit(1)

# CF API execution
h = requests.patch("https://api.cloudflare.com/client/v4/zones/" + CfZoneId + "/dns_records/" + CfDnsRecordId, headers=headers, json=data)
if h.status_code == 200:
    print("Success!")
else:
    print("Fail!")
print(h.json())