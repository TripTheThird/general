
adjective = input('Adjective: ').lower()
animal = input('Animal: ').lower()
verb = input('Verb: ').lower()
exclamation = input('Exclamation: ').capitalize()
verb2 = input('Another Verb: ').lower()
verb3 = input('Another Verb: ').lower()
name = input('A Name: ').upper()

print("\nHere is your finished mad lib!")
print("-----------------------------------------------------------------------------")
print('\nThe other day, I was really in trouble. It all started when I saw a very')
print(f'{adjective} {animal} {verb} down the hallway. "I AM {name}" the {animal} shouted. "{exclamation}!" I yelled, but all')
print(f'I could think to do was to {verb2} over and over. Miraculously,')
print(f'that caused it to stop, but not before it tried to {verb3}')
print('right in front of my family.')