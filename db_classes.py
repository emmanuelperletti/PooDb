import sqlite3 as sql


class User:
    def __init__(self, login, passw, _id=-1):
        self.login = login
        self.password = passw
        self.id = _id

    def save(self):
        if (self.id == -1):
            with sql.connect('db.db') as conn:

                cur = conn.cursor()
                check = Users.get_by_login(self.login)
                if check is not None:
                    print(f"Ajout impossible, un utilisateur avec le login {self.login} existe déjà")
                else:
                    res = cur.execute(f'INSERT INTO users (login, password) VALUES ("{self.login}","{self.password}" )')
                    print("*** Ajout réussi") if res else print("ERR Ajout impossible")
        else:
            with sql.connect('db.db') as conn:
                cur = conn.cursor()
                res = cur.execute(
                    f'UPDATE users SET login = "{self.login}", password ="{self.password}" WHERE id = {self.id}')
                print("*** Modification réussie") if res else print("ERR Modification impossible")

    def remove(self):
        with sql.connect('db.db') as conn:
            cur = conn.cursor()
            res = cur.execute(f'DELETE FROM users WHERE id = {self.id}')
            print("*** Suppression réussie") if res else print("ERR Suppression impossible")

class Users:
    @staticmethod
    def all():
        users = []

        # query db to get users
        with sql.connect('db.db') as conn:
            cur = conn.cursor()
            res = cur.execute('select login, password, id from users')
            for row in res:
                users.append(User(row[0], row[1], row[2]))
        return users

    @staticmethod
    def get_by_id(_id):
        user = None
        with sql.connect('db.db') as conn:
            cur = conn.cursor()
            res = cur.execute(f'select login, password, id from users where id = {_id}')
            for row in res:
                user = User(row[0], row[1], row[2])
        return user

    @staticmethod
    def get_by_login(login):
        user = None
        with sql.connect('db.db') as conn:
            cur = conn.cursor()
            res = cur.execute(f'select login, password, id from users where login = "{login}" LIMIT 1')
            for row in res:
                user = User(row[0], row[1], row[2])
        return user

    @staticmethod
    def reset():
        with sql.connect('db.db') as conn:
            cur = conn.cursor()
            res = cur.execute(f'DELETE FROM users WHERE 1')

