users = list()

users.append({"id": 1, "name": "George", "email": "george@gmail.com", "rol": "Admin", "edad": 52})
users.append({"id": 2, "name": "Paul", "email": "paul@gmail.com", "rol": "Usuario", "edad": 66})
users.append({"id": 3, "name": "Eric", "email": "eric@gmail.com", "rol": "Usuario", "edad": 53})
users.append({"id": 4, "name": "Ringo", "email": "ringo@gmail.com", "rol": "Usuario", "edad": 63})

counter = list()

for i in users:
    if i["rol"] == "Admin":
        print(f"Usuario: {i['name']}, {i['email']}, {i['rol']}")
        counter.append(i)

print(f"Usuarios con rol de Admin: {len(counter)}")

totalUsers = next(u for u in users if u["id"] ==2)

print(f"Usuario con id de 2: {totalUsers}")