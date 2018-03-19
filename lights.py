import time,requests,json

lights = [1,2,3] #IDs of the lights you want to control, from left to right
ip = "IP-OF-YOUR-HUE-Bridge"
username = "YOUR-BRIDGE-USERNAME" # Use get_username.py to get yours

def setLight(idx,x,y,bri):
        if bri != 0:
            #bridge.lights[lights[idx]].state(xy=[x,y],sat=255,bri=int(bri),on=True )
            payload = {
                "sat":255,
                "bri":int(bri),
                "on":True,
                "xy":[x,y]
            }
            resp = requests.put("http://" + ip + "/api/" + username + "/lights/" + str(lights[idx]) + "/state", data=json.dumps(payload))
        else:
            #bridge.lights[lights[idx]].state(xy=[x,y],sat=255,bri=int(bri),on=False )
            payload = {
                "sat":255,
                "bri":int(bri),
                "on":False,
                "xy":[x,y]
            }
            resp = requests.put("http://" + ip + "/api/" + username + "/lights/" + str(lights[idx]) + "/state", data=json.dumps(payload))
        #print "Would set light " + str(lights[idx]) + " X: " + str(x) + " Y: " + str(y) + " BRI: " + str(bri)
        #time.sleep(0.05)
