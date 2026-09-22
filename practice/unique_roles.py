users = [
    {"name": "Eric", "role": "Superadmin"},
    {"name": "George", "role": "Moderador"},
    {"name": "Jhon", "role": "Admin"},
    {"name": "Paul", "role": "Invitado"}
]

unique_roles = []
for u in users:
    if u["role"] not in unique_roles:
        unique_roles.append(u["role"])

print(unique_roles)