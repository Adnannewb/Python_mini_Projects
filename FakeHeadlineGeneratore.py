import random

subjects=[
    "Virat Kohli",
    "PM",
    "VC",
    "Losers",
    "Lion",
]

actions=[
    "declares war on",
    "eats",
    "loses",
    "visits ",
]

places_or_thinngs=[
    "Lalbag",
    "Chicken",
    "Dhaka",
    "Australia",
]

while True:
    subject=random.choice(subjects)
    action=random.choice(actions)
    works=random.choice(places_or_thinngs)
    
    Headline=f" Breaking news : {subject} {action} {works}"
    print(Headline)
    
    user=input("Do you want another Headline ? (yes/no) :").strip().lower()
    if(user=='no'):
        break
    
print("Thank you for using fake headline generator. Have a good day ")    