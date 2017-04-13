#!/usr/bin/env python

import speech_recognition as sr
import time
from gtts import gTTS
import os

with open('gspeech.json', 'r') as myfile:
    GOOGLE_CLOUD_SPEECH_CREDENTIALS=myfile.read()

#with open('Keys/wit_ai.txt', 'r') as myfile:
#    WIT_AI_CREDITENTIALS=myfile.read()

r = sr.Recognizer()
m = sr.Microphone(sample_rate=44100,chunk_size=2048)

print("A moment of silence, please...")
with m as source: r.adjust_for_ambient_noise(source)
print('Recording')
with m as source: audio = r.listen(source)
print('Finished recording')

start_time = time.time()
value_g = r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS, preferred_phrases=['Baxter','tuck','untuck','right','left','open','close'],show_all=True)
elapsed_time_g = time.time() - start_time

tts = gTTS(text=json['msg'], lang='en')
tts.save("temp.mp3")
os.system("mpg321 temp.mp3")
print('Google Time needed: %i Response: %s\n',elapsed_time_g, value_g)