import requests
import json
import pyttsx3 as pyt

if __name__=='__main__':
    print("------->>Welcome to the weather app <<--------\n")
    print("Write Bye to close the app \n")
    
   
    
    
    while True:
        city = input("Enter Your city : ").lower()
        engine = pyt.init()
        engine.setProperty('rate', 150)
        if city == "bye":
            engine.say("Bye bye friend")
            engine.runAndWait()
            break
        
        try:
            url = f"https://api.weatherapi.com/v1/current.json?key=6af7e4768fe248cea6010751250211&q={city}"
            weather = requests.get(url)
            weather.raise_for_status()
            weatherdic = weather.json() 

            text = (
                f"Hi, You want to know about {city} city's today's weather condition. "
                f"Here is the briefing. {city}'s temperature is "
                f"{weatherdic['current']['temp_c']} degree Celsius, and the weather condition is "
                f"{weatherdic['current']['condition']['text']}. Thank you."
            )

            # Speak the weather
            engine.say(text)
            engine.runAndWait()
            # ⚠️ DO NOT CALL engine.stop() HERE

        except requests.exceptions.HTTPError:
            print("Invalid city name, searching suggestions...")
            suggest_url = f"https://api.weatherapi.com/v1/search.json?key=6af7e4768fe248cea6010751250211&q={city}"
            suggestions = requests.get(suggest_url).json()
            if suggestions:
                print("Did you mean:")
                for s in suggestions[:5]:
                    print(s["name"], "-", s["country"])
            else:
                print("No suggestions found.")
            print("Try again\n")
        except Exception:
            print("An error occurred! Check input or network.\n")
