#!/usr/bin/env python3
import cgi
import json
import caesar
# -------------------------- GETTING DATA -------------------------
cgiData = cgi.FieldStorage()
request = cgiData.getfirst('REQUEST')
# request must be in json, so:
data = json.loads(request)
# fields to restore, see frontend.js in sendData() function
message = data['message'].lower()
rotate = int(data['rotate'])
decode = data['decode']
# ------------------------- PROCESSING DATA ------------------------
# choosing decode or encode
handler = caesar.decode if decode else caesar.encode
outputText = handler(message, rotate)
lettersFrequencyDict = caesar.frequency_dict(message)
tryToGuess = caesar.try_to_guess(message)
# -------------------  OUTPUT  -------------------
# let's jsonize answer
response = json.dumps({'outputtext': outputText,
                       'frequencydict': lettersFrequencyDict,
                       'trytoguess': tryToGuess})

print('Content-type: text/html\n')  # requires by standard
print(response)