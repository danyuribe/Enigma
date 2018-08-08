import time
import random




alphabet= ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

rotor1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
rotor2=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
rotor3=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
letterplugs=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
availableletters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
rotor1code=[]
rotor2code=[]
rotor3code=[]
plugsetup=[]
letterswitches=[]
message=[]
encodedmessage=[]
shuffleReps=0
rotations=0
def setupRotor():
    global rotor1
    global rotor2
    global rotor3
    global rotor1code
    global rotor2code
    global rotor3code
    global shuffleReps
    rotor1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    rotor2=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    rotor3=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for s in range(shuffleReps):
        x=random.randint(0,25)
        y=random.randint(0,25)
        rotor1code.append([x,y])
        sub1=rotor1[x]
        rotor1[x]=rotor1[y]
        rotor1[y]=sub1
    for s in range(shuffleReps):
        xx=random.randint(0,25)
        yy=random.randint(0,25)
        rotor2code.append([xx,yy])
        sub2=rotor2[xx]
        rotor2[xx]=rotor2[yy]
        rotor2[yy]=sub2
    for s in range(shuffleReps):
        xxx=random.randint(0,25)
        yyy=random.randint(0,25)
        rotor3code.append([xxx,yyy])
        sub3=rotor3[xxx]
        rotor3[xxx]=rotor3[yyy]
        rotor3[yyy]=sub3
    print(rotor1)
    print(rotor2)
    print(rotor3)
    print (rotor1code)
    print(rotor2code)
    print(rotor3code)
def letterSwitches():
    global plugsetup
    global alphabet
    global letterplugs
    global availableletters
    global letterswitches
    letterplugs=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    availableletters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    while availableletters!=[]:
        a=random.randint(0,25)
        if (alphabet[a] in availableletters) == True:
            availableletters.pop(availableletters.index(alphabet[a]))
            print("Available letters = ",availableletters)
            print("First plug is in letter {}".format(alphabet[a]))
            time.sleep(0.1)
            b=input("Second letter plug:")
            time.sleep(0.2)
            str(b)
            if (b in availableletters) == True:
                sub=letterplugs[letterplugs.index(alphabet[a])]
                letterplugs[letterplugs.index(alphabet[a])]=letterplugs[letterplugs.index(b)]
                letterplugs[letterplugs.index(b)]=sub
                availableletters.pop(availableletters.index(b))
                plugsetup.append([a,alphabet.index(b)])
                letterswitches.append([alphabet[a],b])
                print(letterswitches)
                print(plugsetup)
            else:
                print(availableletters)
                letterplugs=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
                availableletters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
                plugsetup=[]
                letterswitches=[]
                print("Plugboard setup has been reset. Enter one capital letter from the available list only.")
    else:
        pass
                

def rotorRotation():
    global rotations

    if rotations <26:
            shift=rotor1[25]
            rotor1.pop(25)
            rotor1.insert(0,shift)
            rotations +=1
    elif rotations >=26 and i<52:
            shift=rotor2[25]
            rotor2.pop(25)
            rotor2.insert(0,shift)
            rotations+=1
    elif rotations>=52:
            shift=rotor3[25]
            rotor3.pop(25)
            rotor3.insert(0,shift)
            rotations+=1
def rotorDecode():
    pass
def encode(letter):
    str(letter)
    message.append(letter)
    for x in letterswitches:
        if x[0]==letter:
            secondletter=x[1]
        elif x[1]==letter:
            secondletter=x[0]
        else:
            pass
    thirdletter=rotor1[alphabet.index(secondletter)]
    fourthletter=rotor2[alphabet.index(thirdletter)]
    fifthletter=rotor3[alphabet.index(fourthletter)]
    encodedmessage.append(fifthletter)
    return fifthletter

def decode(letter):
    str(letter)
    encodedmessage.append(letter)
    secondletter=alphabet[rotor3.index(letter)]
    thirdletter=alphabet[rotor2.index(secondletter)]  #change to list not code
    fourthletter=alphabet[rotor1.index(thirdletter)]
    for x in letterswitches:
        if x[0]==alphabet[alphabet.index(fourthletter)]:
            final=x[1]
        elif x[1]==alphabet[alphabet.index(fourthletter)]:
            final=x[0]
        else:
            pass
    message.append(final)
    return final
    
def rotorSettings():
    availableletters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    rotor1=[]
    rotor2=[]
    rotor3=[]
    print("To set up rotor 1, enter the letter that corresponds to the prompted letter below. Note: Letters will be prompted in order even though the setup is random")
    time.sleep(0.2)
    while True:
        while len(rotor1)!=26:#separate while loops
            print("Set up rotor 1:")
            time.sleep(0.1)
            print(availableletters)
            letter=input("Enter one letter corresponding to the printed value to set up the rotor. 'Available letters' are provided for reference.")
            str(letter)
            if (letter in alphabet)==True:
                if (letter in availableletters) == True:
                    availableletters.pop(availableletters.index(letter))
                    rotor1.append(letter)
                    print(" ")
                else:
                    print("Enter a valid letter from the available list.")
            elif letter=='ALPHABET':
                rotor1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
            else:
                print ("Enter a valid letter from the available list.")
        availableletters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        while len(rotor2)!=26:
            print("Set up rotor 2:")
            time.sleep(0.1)
            print(availableletters)
            letter=input("Enter one letter corresponding to the printed value to set up the rotor. 'Available letters' are provided for reference.")
            str(letter)
            if (letter in alphabet)==True:
                if (letter in availableletters) == True:
                    availableletters.pop(availableletters.index(letter))
                    rotor2.append(letter)
                    print(" ")
                else:
                    print("Enter a valid letter from the available list.")
            elif letter=='ALPHABET':
                rotor2=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
            else:
                print ("Enter a valid letter from the available list.")
        availableletters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        while len(rotor3)!=26:
            print("Set up rotor 3:")
            time.sleep(0.1)
            print(availableletters)
            letter=input("Enter one letter corresponding to the printed value to set up the rotor. 'Available letters' are provided for reference.")
            str(letter)
            if (letter in alphabet)==True:
                if (letter in availableletters) == True:
                    availableletters.pop(availableletters.index(letter))
                    rotor3.append(letter)
                    print(" ")
                else:
                    print("Enter a valid letter from the available list.")
            elif letter=='ALPHABET':
                rotor3=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
            else:
                print ("Enter a valid letter from the available list.")
        print("Rotor setup and letter plugboard setup is complete")
        print(rotor1)
        print(rotor2)
        print(rotor3)
        time.sleep(0.2)
        break
        
try:
    while True:
        print("Welcome to Enigma, a high security electr-mechanical rotor cipher machine developed by German engineer Arthur Scherbius at the end of World War I to protect military communication. Enigma contains 3 rotors and a plugboad used to provide a systematic coding method using a random setup. The rotors will have a random wiring that is preset. The plugboard is used to randomly switch two letters at a time a total of 13 times. From this, a code will be created in a letter by letter basis.")
        start=input("Encode or decode? (Enter Encode or Decode)")
        str(start)
        if start=='Encode':
            plugsetup=[]
            letterswitches=[]
            message=[]
            encodedmessage=[]
            rotations=0
            state= True
            loops=0
            while state==True:
                if loops==0:
                    setupRotor()
                    print("Enigma's security involves a plugboard that switches two letters in the beginning of the encryption. Both the encoder and the decoder must have the same setup in order for the message to decode correctly. The system will simulate a randomly chosen letter and will prompt a second letter to switch with. Enter a letter from the list provided.")
                    letterSwitches()
                    print("Take note of the following code in order to decode your message.")
                    print(letterswitches)
                    letter=input("Type a letter to encode. Enter CANCEL to end the message.")
                    if (letter in alphabet)==True:
                        print(encode(letter)) 
                        rotorRotation()
                        loops+=1
                        print (rotations)
                    elif letter=='CANCEL':
                        state=False
                        print(message)
                        print(encodedmessage)
                        print(' '.join(message))
                        print(' '.join(encodedmessage))
                        print (rotations)
                    else:
                        loops+=1
                else:
                    letter=input("Type a letter to encode. Enter CANCEL to end the message.")
                    if (letter in alphabet)==True:
                        print(encode(letter)) 
                        rotorRotation()
                        loops+=1
                        print(rotations)
                    elif letter=='CANCEL':
                        state=False
                        print(message)
                        print(encodedmessage)
                        print(' '.join(message))
                        print(' '.join(encodedmessage))
                        print(rotations)
                        print (rotor1)
                    else:
                        loops+=1
        elif start=='Decode':
            letterplugs=[]
            availableletters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
            plugsetup=[]
            letterswitches=[]
            message=[]
            encodedmessage=[]
            rotations=0
            print("In order to accurately decode a message, both Enigma machines must be set exactly the same. Enter the letter plug coordinates in a letter by letter basis according to the code's original setup.")
            letterSwitches()
            print("Plug board setup is the following: {}".format(letterswitches))
            print(" ")
            state=True
            loops=0
            while state==True:
                if loops==0:
                    rotorSettings()
                    letter=input("Type a letter to decode. Enter CANCEL to end the message.") 
                    if (letter in alphabet)==True:
                        print(decode(letter)) 
                        rotorRotation()
                        loops+=1
                        print (rotations)
                    elif letter=='CANCEL':
                        state=False
                        print(encodedmessage)
                        print(message)
                        print(' '.join(message))
                        print(' '.join(encodedmessage))
                        print (rotations)
                    else:
                        loops+=1
                else:
                    letter=input("Type a letter to encode. Enter CANCEL to end the message.")
                    if (letter in alphabet)==True:
                        print(decode(letter)) 
                        rotorRotation()
                        loops+=1
                        print(rotations)
                    elif letter=='CANCEL':
                        state=False
                        print(encodedmessage)
                        print(message)
                        print(' '.join(message))
                        print(' '.join(encodedmessage))
                        print(rotations)
                        print(rotor1)
                    else:
                        loops+=1
            
        else:
            print("Enter Encode or Decode only")
except KeyboardInterrupt:
    pass
