contacts = {
    'number': 4,
    'students':
        [
            {'name':'Sarah Idiot', 'email':'idiot@idiots.org'},
            {'name':'Sarah Dumbass', 'email':'dumbass@idiots.org'},
            {'name':'Sarah Moron', 'email':'moron@idiots.org'},
            {'name':'Sarah The Rube', 'email':'therube@idiots.org'}
        ]
}

print("Student emails:")
for student in contacts['students']:
    print(student['email'])