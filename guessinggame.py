import random 
easy_words = ["apple", "cat", "ball", "book", "sun", "car", "fish", "tree", "shoe", "cake", "rain", "bird", "milk", "chair", "phone"]
medium_words = ["orange", "garden", "rocket", "pillow", "window", "guitar", "jungle", "camera", "farmer", "island", "doctor", "laptop", "castle", "market", "mirror"]
hard_words = ["adventure", "microscope", "electricity", "knowledge", "psychology", "atmosphere", "architecture", "communication", "civilization", "astronaut", "photography", "imagination", "technology", "earthquake", "experiment"]
print(" -------> Welcome to the Guessing Game <-----------\n")
user_input=input("Chosse easy ,medium or hard mode .....").lower()

if(user_input=='easy'):
    secret=random.choice(easy_words)
elif(user_input=='medium'):
    secret=random.choice(medium_words)
else:
    secret=random.choice(hard_words)        
attempts=0  
while True:
    guess=input("Guess your words: \n").strip().lower()
    attempts+=1
    if(guess==secret):
        print(f"Congratulations ,YOU won the game . You completed the whole game in {attempts} attempts.\n")
        break
    hint=''
    for i in range(len(secret)):
        if(i<len(guess) and guess[i]==secret[i]):
            hint +=guess[i]
        else:
            hint+='_'
    print("Hint: ",hint)            
print("GAME OVER")            