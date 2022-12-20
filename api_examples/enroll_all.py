import requests

username = ''
password = ''
base_url = 'http://127.0.0.1:8000/api/'

# Get all courses
req = requests.get(f'{base_url}edufy/')
req.raise_for_status()  # Exception: not 2xx
courses = req.json()
available_courses = ', '.join([course['title'] for course in courses])
print(f'Available courses: {available_courses}')

for course in courses:
    course_id = course['id']
    course_title = course['title']
    req = requests.post(f'{base_url}edufy/{course_id}/enroll/', auth=(username, password))

    if req.status_code == 200:
        # Success
        print(f'Successfully enrolled in..\n{course_title}')
