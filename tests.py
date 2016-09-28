import database

database.init_db()
p = database.getAllPetInfo()
print(p)
