from gtts import gTTS
import os
mytext=" i love you:"
language='en'
myobj=gTTS(text=mytext,lang=language,slow=False)
myobj.save("voi2.mp3")
os.system("voi2.mp3")