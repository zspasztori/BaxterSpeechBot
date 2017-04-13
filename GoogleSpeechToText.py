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
m = sr.Microphone(sample_rate=16000,chunk_size=2048)

print("A moment of silence, please...")
with m as source: r.adjust_for_ambient_noise(source)
print('Recording')
with m as source: audio = r.listen(source)
print('Finished recording')

start_time = time.time()
value_g = r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS, preferred_phrases=['Baxter','tuck','untuck','right','left','open','close'],show_all=True)
elapsed_time_g = time.time() - start_time

text = 'Google Time needed: ' + str("%.2f" % round(elapsed_time_g,1)) + ' seconds'
tts = gTTS(text=text, lang='en')
tts.save("temp.mp3")
print text
#os.system("mpg321 temp.mp3")
print(' Response: %s\n', value_g)