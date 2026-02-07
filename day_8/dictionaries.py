dog = {}
dog['name'] = 'Moni'
dog['color'] = 'brown'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 10
print('dog:', dog)

student = {
    'first_name': 'Jordan',
    'last_name': 'Parra',
    'gender': 'male',
    'age': 29,
    'marital_status': 'married',
    'skills': ['Python', 'JavaScript', 'Apex'],
    'country': 'Colombia',
    'city': 'Bogota',
    'address': 'Cra 0 # 123-45'
}
print('student:', student)
print('Length of student dictionary:', len(student))
print('Skills of student:', student['skills'])
print('Type of skills:', type(student['skills']))
student['skills'].append('LWC')
student['skills'].append('Java')
print('Updated skills of student:', student['skills'])
print('Dictionary keys:', student.keys())
print('Dictionary values:', student.values())
dict_items = student.items()
print('Dictionary items:', dict_items)
print('Dictionary items type:', type(dict_items))
del student['age']
print('Student dictionary after deleting age:', student)
student.clear()
print('Student dictionary after clearing:', student)