import sqlite3

with sqlite3.connect("blog.db") as conn:
	c = conn.cursor()

	c.execute("""CREATE TABLE IF NOT EXISTS posts(title TEXT, post TEXT)""")

	posts = [
			("Good", "Im Good"),
			("Well", "Im Well"),
			("Excellent", "Im excellent"),
			("Okay", "Im okay")
	]

	c.executemany('INSERT INTO posts VALUES(?,?)', posts)

	rows = c.fetchall()

	for r in rows:
		print(r[0], r[1])

