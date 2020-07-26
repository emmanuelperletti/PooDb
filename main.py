from db_classes import Users, User

Users.reset()

u1 = User("Manu", "PwdManu")
u1.save()  # save fait un add car l'id n'est pas défini (-1)
u2 = User("Bob", "PwdBob")
u2.save()
u3 = User("Jeannot", "PwdJeannot")
u3.save()
u4 = User("Gérard", "PwdGérard")
u4.save()

print("-" * 20)
print("Table au démarrage")
userlist = Users.all()  # obtenir tous les users
for user in userlist:
    print(user.login, user.password)

print("-" * 20)
print("Le User qui a le login Bob va devenir Super Bob")
# obtenir un user particulier
u = Users.get_by_login("Bob")
u.login = "Super Bob"
u.save()  # save fait un update car l'id est défini

print("-" * 20)
print("Table après modification de Bob en Super Bob")
userlist = Users.all()  # obtenir tous les users
for user in userlist:
    print(user.login)

print("-" * 20)
print("On supprime Jeannot (et on appelle Léon pour le nettoyage)")
# supprimer un user (Jeannot)
u = Users.get_by_login("Jeannot")
u.remove()

print("-" * 20)
print("Table après passage de Léon")
userlist = Users.all()  # obtenir tous les users
for user in userlist:
    print(user.login)

print("-" * 20)
print("On ajoute un utilisateur existant déjà")
u5 = User("Gérard", "PwdGérard")
u5.save()