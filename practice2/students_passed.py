estudiantes = list()

estudiantes.append({"name": "Eric", "grade": 6})
estudiantes.append({"name": "George", "grade": 4})
estudiantes.append({"name": "Jhon", "grade": 8})
estudiantes.append({"name": "Paul", "grade": 6})

aprobados = list()

for e in estudiantes:
    if e["grade"] >= 7:
        aprobados.append(e["name"])

print(f"Estudiantes que pasaron: {aprobados}")