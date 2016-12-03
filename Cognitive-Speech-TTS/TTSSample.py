import json
import requests
import time
import uuid
from urlparse import urljoin

#Note: The way to get api key:
#Free: https://www.microsoft.com/cognitive-services/en-us/subscriptions?productId=/products/Bing.Speech.Preview
#Paid: https://portal.azure.com/#create/Microsoft.CognitiveServices/apitype/Bing.Speech/pricingtier/S0
apiKey = "3ca8861d0ffc4609b2133a2630a8cabe"
# apiKey = "3d5405654384480780fc1a80c9d9dcbd"

AccessTokenHost = "https://api.cognitive.microsoft.com"
path = "/sts/v1.0/issueToken"
AccessTokenUri = urljoin(AccessTokenHost, path)

# Connect to server to get the Access Token
start = time.time()
print ("Connect to server to get the Access Token")
resp = requests.post(AccessTokenUri, headers={"Ocp-Apim-Subscription-Key": apiKey})
data = resp.content

accesstoken = data.decode("UTF-8")
print ("Access Token: " + accesstoken), time.time() - start


speechServiceUri = "https://speech.platform.bing.com/recognize?{}&{}&{}&{}&{}&{}&{}&{}"
version = 'version=3.0'
locale = 'locale=zh-CN'
device_os = 'device.os=mac'
res_format = 'format=json'
scenarios = 'scenarios=ulm'
appid = 'appid=D4D52672-91D7-4C74-8AD8-42B1D98141A5'
requestid = 'requestid={}'.format(str(uuid.uuid4()))
instanceid = 'instanceid={}'.format(str(uuid.uuid4()))
speechServiceUri = speechServiceUri.format(version, requestid, locale, device_os, res_format, scenarios, appid, instanceid)

headers = {
    "Authorization": "Bearer " + accesstoken,
    "Content-Type": "audio/wav;samplerate=16000"
}

audio_filename = 'audio_1480660331.85.wav'
with open(audio_filename) as f:
    resp = requests.post(speechServiceUri, headers=headers, data=f.read(), verify=False)
    if resp.status_code == 403:
        print 403
    assert resp.status_code == 200 and resp.content
    ret_data = resp.json()
    if 'results' in ret_data:
        for result in ret_data['results']:
            print result, result['name'], len(result['name'])
    print None




