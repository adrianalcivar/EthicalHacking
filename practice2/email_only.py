users = list()

users.append({"id": 1, "name": "Eric", "email": "eric@gmail.com", "rol": "Admin", "edad": 74})
users.append({"id": 2, "name": "George", "email": "george@gmail.com", "rol": "Usuario", "edad": 66})
users.append({"id": 3, "name": "Jhon", "email": "jhon@gmail.com", "rol": "Usuario", "edad": 65})
users.append({"id": 4, "name": "Paul", "email": "paul@gmail.com", "rol": "Usuario", "edad": 65})

emails = list()

for u in users:
    emails.append(u["email"])

print(f"Emails: {emails}")