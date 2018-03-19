import time,requests,json

lights = [1,2,3] #IDs of the lights you want to control, from left to right
ip = "IP-OF-YOUR-HUE-Bridge"
username = "YOUR-BRIDGE-USERNAME" # Use get_username.py to get yours

def setLight(idx,x,y,bri):
        if bri != 0:
            payload = {
                "sat":255,
                "bri":int(bri),
                "on":True,
                "xy":[x,y]
            }
            resp = requests.put("http://" + ip + "/api/" + username + "/lights/" + str(lights[idx]) + "/state", data=json.dumps(payload))
        else:
            payload = {
                "sat":255,
                "bri":int(bri),
                "on":False,
                "xy":[x,y]
            }
            resp = requests.put("http://" + ip + "/api/" + username + "/lights/" + str(lights[idx]) + "/state", data=json.dumps(payload))
