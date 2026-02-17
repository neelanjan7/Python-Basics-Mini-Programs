def hello_func(greeting, name = 'you' ):
    return '{}, {}.'.format(greeting, name)

print (hello_func('Hi'))



def student_info(*args, **kwargs):
    print (args)
    print (kwargs)

courses = ['Math', 'Arts']
info = {'name' :'John', 'age' : 25 }

student_info(*courses, **info)

