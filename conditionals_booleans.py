language = 'java'

if language == 'python':
    print('Language is Python')

elif language == 'java':
    print('Language is Java')

else:
    print ('no match')




user = 'admin'
logged_in = False
if user == 'admin' and logged_in :
    print('Admin Page')
else :
    print('Bad creds')

if user == 'admin' or logged_in :
    print('Admin Page')
else :
    print('Bad creds')

if not logged_in :
    print ('Please log in')
else : 
    print ('Welcome')


