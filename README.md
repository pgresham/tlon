# tlon
Hlör U Fang Axaxaxas Mlö

Based on a passage from Borges' short story Tlön, Uqbar, Orbis Tertius, the proposed installation listens to speech in an area immediately under the device, strips all nouns and proper names from the data, then projects the words on an adjacent wall. As humanity holds the naming of things to be a factor which sets us apart from nature, the resultant text becomes a narrative of universal feeling rather than direct description. 

The python script relies on Alpha Cephi's Vosk package to do the work of generating text from speech. The resultant text is then scanned for nouns and proper names referenced from a wordlist. The resultant text is then printed to the screen in a sort of run on sentence of pure feeling and action rather than subjective ideation. 


The intended platform for this project is a Raspberry Pi, though testing in a Windows 10 environment also yielded favorable results.

A word on extended funcitionality:
Toward the botton of Tlon.py, there are some commented out sections to allow funcitons such as exiting when "goodbye" is heard and printing all text regardless of wordlist for testing purposes. These were left in here as they represent other abilities of the speech processor and could prove useful to anyone wishing to use and/or modify the code. In one instance, the "goodbye" function was changed to print an ascii image of the author at the end of a talk when the processor heard "any questions?" Suffice it to say it was a hit.
