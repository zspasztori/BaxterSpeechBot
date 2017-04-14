#!/usr/bin/env python

import speech_recognition as sr
import time
from gtts import gTTS
import os
import apiai
import uuid
import json
import botActions

botDo =botActions.botActions()

with open('gspeech.json', 'r') as myfile:
    GOOGLE_CLOUD_SPEECH_CREDENTIALS=myfile.read()

ai = apiai.ApiAI('e04adfd76c294f628762d676927ff97c')


r = sr.Recognizer()
m = sr.Microphone(sample_rate=16000,chunk_size=2048)

print("A moment of silence, please...")
with m as source: r.adjust_for_ambient_noise(source)

session_over  = False

while not session_over:

    #Recording audio
    print('Recording')
    with m as source: audio = r.listen(source)
    print('Finished recording')

    start_time = time.time()
    value_g = r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS, preferred_phrases=['Baxter','tuck','untuck','right','left','open','close','wave'],show_all=True)
    elapsed_time_g = time.time() - start_time
    print('Google Time needed: %i Response: %s\n', elapsed_time_g, value_g)

    #Getting the response from api.ai
    request = ai.text_request()
    request.session_id = str(uuid.uuid1())
    try:
        user_question = value_g['results'][0]['alternatives'][0]['transcript']
    except KeyError:
        user_question = ''
    request.query = value_g['results'][0]['alternatives'][0]['transcript']
    response = request.getresponse()
    response_text = response.read()
    json_resp = json.loads(response_text)
    print(response_text)

    #Invoking action
    actionPerform = json_resp['result']['action']
    if actionPerform in botDo.actions:
        context = botDo.actions[actionPerform](json_resp)
    if actionPerform == 'aSessionOver':
        session_over = True

    #Giving voice response
    text_out = json_resp['result']['fulfillment']['speech']
    if text_out:
        tts = gTTS(text=text_out, lang='en')
        tts.save("temp.mp3")
        os.system("mpg321 temp.mp3")
