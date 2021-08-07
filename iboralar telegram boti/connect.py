import   sqlite3
class DBHelper:
	def __init__(self,db_name):
		self.conn=sqlite3.connect(db_name,check_same_thread=False)
		self.conn.row_factory=sqlite3.Row
		self.cursor=self.conn.cursor()

	def get_regions(self):
		# print('assskdjsjjakjka  diskskskkscks')
		return self.cursor.execute('SELECT id, ibora,meaning FROM iboralar order by id asc limit 60').fetchall()
	def get_meaning(self,id):
		return self.cursor.execute(f"SELECT meaning FROM iboralar WHERE id=={id}").fetchone()