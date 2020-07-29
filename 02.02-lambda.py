people = [
    {"name": "Munish", "city": "GZB"},
    {"name": "Ravish", "city": "LKO"},
    {"name": "Satish", "city": "DEL"},
    {"name": "Ashish", "city": "FBD"},
    {"name": "Rajesh", "city": "GKP"}
]


"""
def keyName(person):
    return person["name"]

def keyCity(person):
    return person["city"]

people.sort( key = keyCity )

 """

people.sort( key = lambda person : person["name"] )
#people.sort( key = lambda person : person["city"] )

print(people)