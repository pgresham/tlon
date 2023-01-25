import queue
import sounddevice
import vosk
import json
import os
import sys
from art import tprint



q = queue.Queue()

def callback(indata,frames,time,status):
    if status:
        print(status,file=sys.stderr)
    q.put(bytes(indata))


if os.name == 'nt':
	def clear():
		os.system('cls')
else:
	def clear():
		os.system('clear')


###The following function creates the wordlist from specified file fname
def wordlist(fname):
    words = []
    try:
        with open(fname,'r') as v:
            for i in v:
                words.append(i.strip('\n'))
            v.close()
        return words
    except Exception as e:
        print(e)
        exit(0)
try:
    model = vosk.Model('vosk-model-small-en-us-0.15')   #Edit this if different model. Folder must be in same directory as this file.
    
    #As a sidenote, the small size vosk model is used here in lieu of the full size 
    #as a Dell Inspiron with Intel Core 2 processor and 4GB of RAM that was used to 
    #develop and test this code. The device runs out of memory before fully loading
    #the full size model. As this is intended to be run on a RaspberryPi or
    #similar platform, it is recommended that vosk-small models be used to ensure
    #program functionality.
   

###NOTE run sounddevice.query_devices() on console to list devices available
###This will likely be necessary when installing on a new platform and will
###be more completely spelled out in the readme

    device_info=sounddevice.query_devices(None,'input')
    samplerate=int(device_info['default_samplerate'])
    


###This loads all the depenencies for the input
    with sounddevice.RawInputStream(
        samplerate=samplerate,
        blocksize = 8000,#8000
        device = None,
        dtype = 'int16',
        channels = 1,
        callback = callback):
        
        rec = vosk.KaldiRecognizer(model,samplerate)
###clears out the loading messages
        clear() 



###NOTE Change variable words to alter noun list.
###Eventually migrate this to args

        words = wordlist('wordlist.txt') 

### Main Loop ###

        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                parsed=json.loads(rec.Result())
                text = str(parsed['text']).split(' ')


###This will print only if the words are in the verblist
                for i in text:
###Clearing clause: possibly modify stdin options to allow phrase to be user specified
                    if i == 'erase':
                        clear()

###Program is set to EXCLUDE words in list
                    elif i not in words:
                        sys.stdout.write(i)
                        sys.stdout.write(' ')
                    else:
                        pass
                sys.stdout.flush()


###This will print the text all as one line without checking wordlist  
               # sys.stdout.write(text)
               # sys.stdout.flush()
    

###This will print the text with newline after each 'phrase'
              
               # print(text)
      

###Following is an example of basic commands that can be enabled:

                    #if text == 'exit':
                        #print('\nGoodbye!')
                        #exit(0)

            else:
                pass

except KeyboardInterrupt:
    clear()
    print('\nGoodbye')
    exit(0)
except Exception as e:
    print(str(type(e))+' '+str(e))
    exit(0)


