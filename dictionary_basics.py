character = {'name' : 'K', 'age' : 35, 'city' : 'Los Angeles', 'job' : ['Blade Runner', 'LAPD'] }
print(character['job'])

print(character.get('height', 'Height not found'))

character['phone'] = '9334423333'


character.update({'age' : 36, 'phone' : '1234-4321'})
print(character.keys())

for value, key in character.items():
    print(key, ":" , value)

if character ['age'] >= 18:
    print("K")
else:   print("Not K")

