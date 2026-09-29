users = list()

users.append({"id": 1, "name": "Eric", "email": "eric@gmail.com", "rol": "Admin", "edad": 74})
users.append({"id": 2, "name": "George", "email": "george@gmail.com", "rol": "Usuario", "edad": 66})
users.append({"id": 3, "name": "Jhon", "email": "jhon@gmail.com", "rol": "Usuario", "edad": 65})
users.append({"id": 4, "name": "Paul", "email": "paul@gmail.com", "rol": "Usuario", "edad": 65})

def find_user_by_email(users, email):
    return next((u for u in users if u["email"] == email), None)

resultado = find_user_by_email(users, "jandry@gmail.com")
print(f"Usuario encontrado: {resultado}")

resultado2 = find_user_by_email(users, "no-existe@gmail.com")
print(f"Usuario encontrado: {resultado2}")