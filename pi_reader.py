import pickle

characters = pickle.load(open("resources/char", 'rb'))

#print(characters)
print()

for character in characters:
    print(characters[character])

print()
print(characters)
