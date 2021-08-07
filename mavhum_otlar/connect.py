import sqlite3
db_name='db.db'

class Databasa:
    def search(self,word):
        try:
            conn=sqlite3.connect(db_name)
            cursor=conn.cursor()
            cursor.execute(f"""SELECT meaning FROM lugat
                                WHERE words="{word}" """)
            return cursor.fetchone()

        except Exception as e:
            print('xatolik1: ',e)
    def help(self,id):
        cod = self.read()[0]
        # print(cod)
        try:
            conn=sqlite3.connect(db_name)
            cursor=conn.cursor()
            cursor.execute(f"DELETE FROM help WHERE code={cod}")
            cursor.execute(f"""INSERT INTO help(code) VALUES({id})""")
            conn.commit()
            conn.close()
            return True

        except Exception as e:
            print('xatolik2: ',e)
    def read(self):
        try:
            conn=sqlite3.connect(db_name)
            cursor=conn.cursor()
            cursor.execute(f"""SELECT code FROM help""")
            return cursor.fetchone()

        except Exception as e:
            print('xatolik: ',e)
