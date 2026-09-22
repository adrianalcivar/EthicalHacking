student = [
    {"name": "Eric", "present": True},
    {"name": "George", "present": False},
    {"name": "Jhon", "present": False}
]

for alumno in student:
    if not alumno["present"]:
        print(alumno["name"])