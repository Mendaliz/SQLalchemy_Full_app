from requests import get, post, delete

# print(get('http://localhost:5000/api/v2/jobs').json())
#
# print(get('http://localhost:5000/api/v2/jobs/1').json())
#
# print(get('http://localhost:5000/api/v2/jobs/999').json())
# # новости с id = 999 нет в базе
#
# print(get('http://localhost:5000/api/v2/jobs/q').json())
#
# print(post('http://localhost:5000/api/v2/jobs', json={}).json())
#
# print(post('http://localhost:5000/api/v2/jobs',
#            json={'team_leader': 1}).json())
#
# print(post('http://localhost:5000/api/v2/jobs',
#            json={'team_leader': 1,
#                  'job': 'connect 3 and 4 work modules',
#                  'work_size': 4,
#                  'collaborators': '2, 3',
#                  'is_finished': True}).json())
#
# print(get('http://localhost:5000/api/v2/jobs').json())
#
# print(delete('http://localhost:5000/api/v2/jobs/999').json())
# # новости с id = 999 нет в базе
#
# print(delete('http://localhost:5000/api/v2/jobs/3').json())
#
# print(get('http://localhost:5000/api/v2/jobs').json())
