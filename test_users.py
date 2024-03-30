from requests import get, post, delete, put

# print(get('http://localhost:5000/api/users').json())
#
# print(get('http://localhost:5000/api/users/1').json())
#
# print(get('http://localhost:5000/api/users/999').json())
# # новости с id = 999 нет в базе
#
# print(get('http://localhost:5000/api/users/q').json())

# print(post('http://localhost:5000/api/users', json={}).json())
#
# print(post('http://localhost:5000/api/users',
#            json={'surname': 'Vivzie'}).json())
#
# print(post('http://localhost:5000/api/users',
#            json={'surname': 'Pilgrim',
#                  'name': 'Zlata',
#                  'age': 19,
#                  'position': 'cook',
#                  'speciality': 'biology engineer',
#                  'address': 'module_3',
#                  'email': 'Zlata_cookie@mars.org',
#                  'hashed_password': 'gold'}).json())
#
# print(get('http://localhost:5000/api/users').json())
#
# print(delete('http://localhost:5000/api/users/999').json())
# # новости с id = 999 нет в базе
#
# print(delete('http://localhost:5000/api/users/5').json())
#
# print(get('http://localhost:5000/api/users').json())
#
# print(put('http://localhost:5000/api/users/5',
#           json={'is_finished': False}).json())
#
# print(put('http://localhost:5000/api/users/99',
#           json={'surname': 'Pilgrim',
#                 'name': 'Zlata',
#                 'age': 19,
#                 'position': 'cook',
#                 'speciality': 'biology engineer',
#                 'address': 'module_2',
#                 'email': 'Zlata_cookie@mars.org',
#                 'hashed_password': 'gold'}).json())
#
# print(put('http://localhost:5000/api/users/5',
#           json={'surname': 'Pilgrim',
#                 'name': 'Zlata',
#                 'age': 19,
#                 'position': 'cook',
#                 'speciality': 'biology engineer',
#                 'address': 'module_5',
#                 'email': 'Zlata_cookie@mars.org',
#                 'hashed_password': 'gold'}).json())
#
# print(get('http://localhost:5000/api/users').json())
