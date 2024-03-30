from requests import get, post, delete, put

print(get('http://localhost:5000/api/jobs').json())

print(get('http://localhost:5000/api/jobs/1').json())

print(get('http://localhost:5000/api/jobs/999').json())
# новости с id = 999 нет в базе

print(get('http://localhost:5000/api/jobs/q').json())

print(post('http://localhost:5000/api/jobs', json={}).json())

print(post('http://localhost:5000/api/jobs',
           json={'team_leader': 1}).json())

print(post('http://localhost:5000/api/jobs',
           json={'team_leader': 1,
                 'job': 'connect 3 and 4 work modules',
                 'work_size': 4,
                 'collaborators': '2, 3',
                 'is_finished': True}).json())

print(get('http://localhost:5000/api/jobs').json())

print(delete('http://localhost:5000/api/jobs/999').json())
# новости с id = 999 нет в базе

print(delete('http://localhost:5000/api/jobs/3').json())

print(get('http://localhost:5000/api/jobs').json())

print(put('http://localhost:5000/api/jobs/3',
          json={'is_finished': False}).json())

print(put('http://localhost:5000/api/jobs/99',
          json={'team_leader': 1,
                'job': 'connect 3 and 4 work modules',
                'work_size': 4,
                'collaborators': '2, 3, 5',
                'is_finished': True}).json())

print(put('http://localhost:5000/api/jobs/3',
          json={'team_leader': 1,
                'job': 'connect 3 and 4 work modules',
                'work_size': 4,
                'collaborators': '2, 3, 4',
                'is_finished': True}).json())

print(get('http://localhost:5000/api/jobs').json())
