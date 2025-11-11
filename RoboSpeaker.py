import pyttsx3 as pyt
if __name__=="__main__":
    print("Welcome to Robo Speaker ")
    while(True):
        
        x=input("Enter what you want me to say ... :")
        engine = pyt.init()
        if(x=='bye' or x=='Bye'):
            engine.say("Bye bye friend")
            engine.runAndWait()
            break
        else:
            engine.say(x)
            engine.runAndWait()   
                            
                           


