import apiai
import uuid
import json

ai = apiai.ApiAI('e04adfd76c294f628762d676927ff97c')
request = ai.text_request()
request.session_id = str(uuid.uuid1())
request.query = 'Please wave your left hand!'
response = request.getresponse()


response_text = response.read()

#print (response_text)

json_resp = json.loads(response_text)

print response_text
print json_resp['result']['fulfillment']['speech']
print json_resp['result']['action']
print type(json_resp['result']['parameters'])
