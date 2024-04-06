from requests import get, post, delete

print(get('http://localhost:5000/api/v2/users').json())
#
# print(get('http://localhost:5000/api/v2/users/1').json())
#
# print(get('http://localhost:5000/api/v2/users/999').json())
# # новости с id = 999 нет в базе
#
# print(get('http://localhost:5000/api/v2/users/q').json())
#
# print(post('http://localhost:5000/api/v2/users', json={}).json())
#
# print(post('http://localhost:5000/api/v2/users',
#            json={'surname': 'Vivzie'}).json())
#
# print(post('http://localhost:5000/api/v2/users',
#            json={'surname': 'Pilgrim',
#                  'name': 'Zlata',
#                  'age': 19,
#                  'position': 'cook',
#                  'speciality': 'biology engineer',
#                  'address': 'module_3',
#                  'email': 'Zlata_cookie@mars.org',
#                  'hashed_password': 'gold'}).json())
#
# print(get('http://localhost:5000/api/v2/users').json())
#
# print(delete('http://localhost:5000/api/v2/users/999').json())
# # новости с id = 999 нет в базе
#
# print(delete('http://localhost:5000/api/v2/users/5').json())
#
# print(get('http://localhost:5000/api/v2/users').json())
